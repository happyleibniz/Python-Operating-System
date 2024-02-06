import subprocess
import sys
import time


class UnknownError(Exception):
    def __init__(self):
        Exception.__init__(self)


class Terminal(object):
    def __init__(self):
        print("initializing Terminal...")
        print("trying to start pyglet...")
        try:
            import pyglet
        except ImportError:
            print("pyglet is not installed")
            Pyglet_Is_Needed_To_Be_Installed = input("Do you want to install pyglet?(y/n)")
            try:
                if Pyglet_Is_Needed_To_Be_Installed == "y" or Pyglet_Is_Needed_To_Be_Installed == "Y":
                    subprocess.check_output("pip3 install pyglet")
                else:
                    print("thank you for using, but pyglet is not installed, Exiting in four seconds")
                    time.sleep(4)
                    sys.exit("Dependencies not installed")
            except ValueError:
                print(
                    "you need to install pyglet,thank you for using, but pyglet is not installed, Exiting in four "
                    "seconds"
                )
                time.sleep(4)
                sys.exit("Dependencies not installed")
        except not ImportError as e:
            print("some thing is wrong, pyglet is not installed,please try again later")
            raise UnknownError(e)
