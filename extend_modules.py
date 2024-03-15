def download_install_mc():
    print("Downloading metadata...")
    print("Obtaining file")
    import sys
    print("loading module tqdm...")
    try:
        from tqdm import tqdm
    except ModuleNotFoundError:
        print("No Module named tqdm,please install it with pip3 install tqdm")
        sys.exit(403)

    import requests
    url = "https://happyleibniz.github.io/PyOS_files/McPY.zip"
    r = requests.get(url, stream=True)
    filename = url.split('/')[-1]
    with open("Disk/Users/System/Downloads/" + filename, 'wb') as file, tqdm(
            desc=filename,
            total=int(r.headers.get('content-length', 0)),
            unit='iB',
            unit_scale=True,
            unit_divisor=1024, ) as bar:
        for data in r.iter_content(chunk_size=1024):
            size = file.write(data)
            bar.update(size)
        file.close()
    from zipfile import ZipFile
    with ZipFile("Disk/Users/System/Downloads/" + filename, 'r') as zpfile:
        zpfile.extractall(path="Disk\\Program Files\\Minecraft")
    sys.exit()