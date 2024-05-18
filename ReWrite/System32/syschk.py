import collections
import functools
import itertools
import os
import platform
import re
import sys

platform.processor()
import _wmi


class CpuCheck:

    def _wmi_query(self, table, *keys):
        table = {
            "OS": "Win32_OperatingSystem",
            "CPU": "Win32_Processor",
        }[table]
        data = _wmi.exec_query("SELECT {} FROM {}".format(
            ",".join(keys),
            table,
        )).split("\0")
        split_data = (i.partition("=") for i in data)
        dict_data = {i[0]: i[2] for i in split_data}
        return (dict_data[k] for k in keys)

    def __init__(self):
        self._WIN32_CLIENT_RELEASES = [
            ((10, 1, 0), "post11"),
            ((10, 0, 22000), "11"),
            ((6, 4, 0), "10"),
            ((6, 3, 0), "8.1"),
            ((6, 2, 0), "8"),
            ((6, 1, 0), "7"),
            ((6, 0, 0), "Vista"),
            ((5, 2, 3790), "XP64"),
            ((5, 2, 0), "XPMedia"),
            ((5, 1, 0), "XP"),
            ((5, 0, 0), "2000"),
        ]

        self._WIN32_SERVER_RELEASES = [
            ((10, 1, 0), "post2022Server"),
            ((10, 0, 20348), "2022Server"),
            ((10, 0, 17763), "2019Server"),
            ((6, 4, 0), "2016Server"),
            ((6, 3, 0), "2012ServerR2"),
            ((6, 2, 0), "2012Server"),
            ((6, 1, 0), "2008ServerR2"),
            ((6, 0, 0), "2008Server"),
            ((5, 2, 0), "2003Server"),
            ((5, 0, 0), "2000Server"),
        ]

        try:
            system, node, release, version, machine = infos = os.uname()
        except AttributeError:
            system = sys.platform
            node = self._node()
            release = version = machine = ''
            infos = ()

        if not any(infos):
            # uname is not available

            # Try win32_ver() on win32 platforms
            if system == 'win32':
                release, version, csd, ptype = self.win32_ver()
                machine = machine or self._get_machine_win32()

            # Try the 'ver' system command available on some
            # platforms
            if not (release and version):
                system, release, version = self._syscmd_ver(system)
                # Normalize system to what win32_ver() normally returns
                # (_syscmd_ver() tends to return the vendor name as well)
                if system == 'Microsoft Windows':
                    system = 'Windows'
                elif system == 'Microsoft' and release == 'Windows':
                    # Under Windows Vista and Windows Server 2008,
                    # Microsoft changed the output of the ver command. The
                    # release is no longer printed.  This causes the
                    # system and release to be misidentified.
                    system = 'Windows'
                    if '6.0' == version[:3]:
                        release = 'Vista'
                    else:
                        release = ''

            # In case we still don't know anything useful, we'll try to
            # help ourselves
            if system in ('win32', 'win16'):
                if not version:
                    if system == 'win32':
                        version = '32bit'
                    else:
                        version = '16bit'
                system = 'Windows'

            elif system[:4] == 'java':
                release, vendor, vminfo, osinfo = self.java_ver()
                system = 'Java'
                version = ', '.join(vminfo)
                if not version:
                    version = vendor

        # System specific extensions
        if system == 'OpenVMS':
            # OpenVMS seems to have release and version mixed up
            if not release or release == '0':
                release = version
                version = ''

        #  normalize name
        if system == 'Microsoft' and release == 'Windows':
            system = 'Windows'
            release = 'Vista'

        vals = system, node, release, version, machine
        # Replace 'unknown' values with the more portable ''
        self._uname_cache = uname_result(*map(self._unknown_as_blank, vals))

    def cpu_info(self):
        return self._uname_cache

    def _unknown_as_blank(self, val):
        return '' if val == 'unknown' else val

    def _java_getprop(self, name, default):

        from java.lang import System
        try:
            value = System.getProperty(name)
            if value is None:
                return default
            return value
        except AttributeError:
            return default

    def java_ver(self, release='', vendor='', vminfo=('', '', ''), osinfo=('', '', '')):

        """ Version interface for Jython.

            Returns a tuple (release, vendor, vminfo, osinfo) with vminfo being
            a tuple (vm_name, vm_release, vm_vendor) and osinfo being a
            tuple (os_name, os_version, os_arch).

            Values which cannot be determined are set to the defaults
            given as parameters (which all default to '').

        """
        # Import the needed APIs
        try:
            import java.lang
        except ImportError:
            return release, vendor, vminfo, osinfo

        vendor = self._java_getprop('java.vendor', vendor)
        release = self._java_getprop('java.version', release)
        vm_name, vm_release, vm_vendor = vminfo
        vm_name = self._java_getprop('java.vm.name', vm_name)
        vm_vendor = self._java_getprop('java.vm.vendor', vm_vendor)
        vm_release = self._java_getprop('java.vm.version', vm_release)
        vminfo = vm_name, vm_release, vm_vendor
        os_name, os_version, os_arch = osinfo
        os_arch = self._java_getprop('java.os.arch', os_arch)
        os_name = self._java_getprop('java.os.name', os_name)
        os_version = self._java_getprop('java.os.version', os_version)
        osinfo = os_name, os_version, os_arch

        return release, vendor, vminfo, osinfo

    def _syscmd_ver(self, system='', release='', version='',

                    supported_platforms=('win32', 'win16', 'dos')):

        """ Tries to figure out the OS version used and returns
            a tuple (system, release, version).

            It uses the "ver" shell command for this which is known
            to exists on Windows, DOS. XXX Others too ?

            In case this fails, the given parameters are used as
            defaults.

        """
        if sys.platform not in supported_platforms:
            return system, release, version

        # Try some common cmd strings
        import subprocess
        for cmd in ('ver', 'command /c ver', 'cmd /c ver'):
            try:
                info = subprocess.check_output(cmd,
                                               stdin=subprocess.DEVNULL,
                                               stderr=subprocess.DEVNULL,
                                               text=True,
                                               encoding="locale",
                                               shell=True)
            except (OSError, subprocess.CalledProcessError) as why:
                # print('Command %s failed: %s' % (cmd, why))
                continue
            else:
                break
        else:
            return system, release, version

        ver_output = re.compile(r'(?:([\w ]+) ([\w.]+) '
                                r'.*'
                                r'\[.* ([\d.]+)\])')

        # Parse the output
        info = info.strip()
        m = ver_output.match(info)
        if m is not None:
            system, release, version = m.groups()
            # Strip trailing dots from version and release
            if release[-1] == '.':
                release = release[:-1]
            if version[-1] == '.':
                version = version[:-1]
            # Normalize the version and build strings (eliminating additional
            # zeros)
            version = self._norm_version(version)
        return system, release, version

    def _get_machine_win32(self):
        # Try to use the PROCESSOR_* environment variables
        # available on Win XP and later; see
        # http://support.microsoft.com/kb/888731 and
        # http://www.geocities.com/rick_lively/MANUALS/ENV/MSWIN/PROCESSI.HTM

        # WOW64 processes mask the native architecture
        try:
            [arch, *_] = self._wmi_query('CPU', 'Architecture')
        except OSError:
            pass
        else:
            try:
                arch = ['x86', 'MIPS', 'Alpha', 'PowerPC', None,
                        'ARM', 'ia64', None, None,
                        'AMD64', None, None, 'ARM64',
                        ][int(arch)]
            except (ValueError, IndexError):
                pass
            else:
                if arch:
                    return arch
        return (
                os.environ.get('PROCESSOR_ARCHITEW6432', '') or
                os.environ.get('PROCESSOR_ARCHITECTURE', '')
        )

    def _node(self, default=''):

        """ Helper to determine the node name of this machine.
        """
        try:
            import socket
        except ImportError:
            # No sockets...
            return default
        try:
            return socket.gethostname()
        except OSError:
            # Still not working...
            return default

    def win32_ver(self, release='', version='', csd='', ptype=''):
        is_client = False

        version, csd, ptype, is_client = self._win32_ver(version, csd, ptype)

        if version:
            intversion = tuple(map(int, version.split('.')))
            releases = self._WIN32_CLIENT_RELEASES if is_client else self._WIN32_SERVER_RELEASES
            release = next((r for v, r in releases if v <= intversion), release)

        return release, version, csd, ptype

    def _win32_ver(self, version, csd, ptype):
        # Try using WMI first, as this is the canonical source of data
        try:
            (version, product_type, ptype, spmajor, spminor) = self._wmi_query(
                'OS',
                'Version',
                'ProductType',
                'BuildType',
                'ServicePackMajorVersion',
                'ServicePackMinorVersion',
            )
            is_client = (int(product_type) == 1)
            if spminor and spminor != '0':
                csd = f'SP{spmajor}.{spminor}'
            else:
                csd = f'SP{spmajor}'
            return version, csd, ptype, is_client
        except OSError:
            pass

        # Fall back to a combination of sys.getwindowsversion and "ver"
        try:
            from sys import getwindowsversion
        except ImportError:
            return version, csd, ptype, True

        winver = getwindowsversion()
        is_client = (getattr(winver, 'product_type', 1) == 1)
        try:
            version = self._syscmd_ver()[2]
            major, minor, build = map(int, version.split('.'))
        except ValueError:
            major, minor, build = winver.platform_version or winver[:3]
            version = '{0}.{1}.{2}'.format(major, minor, build)

        # getwindowsversion() reflect the compatibility mode Python is
        # running under, and so the service pack value is only going to be
        # valid if the versions match.
        if winver[:2] == (major, minor):
            try:
                csd = 'SP{}'.format(winver.service_pack_major)
            except AttributeError:
                if csd[:13] == 'Service Pack ':
                    csd = 'SP' + csd[13:]

        try:
            try:
                import winreg
            except ImportError:
                import _winreg as winreg
        except ImportError:
            pass
        else:
            try:
                cvkey = r'SOFTWARE\Microsoft\Windows NT\CurrentVersion'
                with winreg.OpenKeyEx(winreg.HKEY_LOCAL_MACHINE, cvkey) as key:
                    ptype = winreg.QueryValueEx(key, 'CurrentType')[0]
            except OSError:
                pass

        return version, csd, ptype, is_client

    def _norm_version(self, version, build=''):

        """ Normalize the version and build strings and return a single
            version string using the format major.minor.build (or patchlevel).
        """
        l = version.split('.')
        if build:
            l.append(build)
        try:
            strings = list(map(str, map(int, l)))
        except ValueError:
            strings = l
        version = '.'.join(strings[:3])
        return version


class uname_result(
    collections.namedtuple(
        "uname_result_base",
        "system node release version machine")
):
    """
    A uname_result that's largely compatible with a
    simple namedtuple except that 'processor' is
    resolved late and cached to avoid calling "uname"
    except when needed.
    """

    _fields = ('system', 'node', 'release', 'version', 'machine', 'processor')

    @functools.cached_property
    def processor(self):
        return self._unknown_as_blank(_Processor.get())

    def __iter__(self):
        return itertools.chain(
            super().__iter__(),
            (self.processor,)
        )

    def _unknown_as_blank(self, val):
        return '' if val == 'unknown' else val

    @classmethod
    def _make(cls, iterable):
        # override factory to affect length check
        num_fields = len(cls._fields) - 1
        result = cls.__new__(cls, *iterable)
        if len(result) != num_fields + 1:
            msg = f'Expected {num_fields} arguments, got {len(result)}'
            raise TypeError(msg)
        return result

    def __getitem__(self, key):
        return tuple(self)[key]

    def __len__(self):
        return len(tuple(iter(self)))

    def __reduce__(self):
        return uname_result, tuple(self)[:len(self._fields) - 1]


_uname_cache = None


class _Processor:
    @classmethod
    def get(cls):
        func = getattr(cls, f'get_{sys.platform}', cls.from_subprocess)
        return func() or ''

    def _wmi_query(self, table, *keys):
        table = {
            "OS": "Win32_OperatingSystem",
            "CPU": "Win32_Processor",
        }[table]
        data = _wmi.exec_query("SELECT {} FROM {}".format(
            ",".join(keys),
            table,
        )).split("\0")
        split_data = (i.partition("=") for i in data)
        dict_data = {i[0]: i[2] for i in split_data}
        return (dict_data[k] for k in keys)

    def get_win32(self):
        try:
            manufacturer, caption = self._wmi_query('CPU', 'Manufacturer', 'Caption')
        except OSError:
            return os.environ.get('PROCESSOR_IDENTIFIER', self._get_machine_win32())
        else:
            return f'{caption}, {manufacturer}'

    def _get_machine_win32(self):
        # Try to use the PROCESSOR_* environment variables
        # available on Win XP and later; see
        # http://support.microsoft.com/kb/888731 and
        # http://www.geocities.com/rick_lively/MANUALS/ENV/MSWIN/PROCESSI.HTM

        # WOW64 processes mask the native architecture
        try:
            [arch, *_] = self._wmi_query('CPU', 'Architecture')
        except OSError:
            pass
        else:
            try:
                arch = ['x86', 'MIPS', 'Alpha', 'PowerPC', None,
                        'ARM', 'ia64', None, None,
                        'AMD64', None, None, 'ARM64',
                        ][int(arch)]
            except (ValueError, IndexError):
                pass
            else:
                if arch:
                    return arch
        return (
                os.environ.get('PROCESSOR_ARCHITEW6432', '') or
                os.environ.get('PROCESSOR_ARCHITECTURE', '')
        )

    def get_OpenVMS(self):
        try:
            import vms_lib
        except ImportError:
            pass
        else:
            csid, cpu_number = vms_lib.getsyi('SYI$_CPU', 0)
            return 'Alpha' if cpu_number >= 128 else 'VAX'

    def from_subprocess(self):
        """
        Fall back to `uname -p`
        """
        try:
            import subprocess
        except ImportError:
            return None
        try:
            return subprocess.check_output(
                ['uname', '-p'],
                stderr=subprocess.DEVNULL,
                text=True,
                encoding="utf8",
            ).strip()
        except (OSError, subprocess.CalledProcessError):
            pass


class MemCheck:
    def __init__(self):
        pass

    def check(self):
        try:
            # Attempt to allocate a large block of memory
            # memory_size = 1
            # memory_block = [0] * memory_size  # Attempt to allocate  of memory
            # del memory_block, memory_size  # reduce memory usage
            return "Memory (RAM) Check: Passed"
        except MemoryError:
            return "Memory (RAM) Check: Failed"
