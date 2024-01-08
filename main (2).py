import os
import time

def check_and_setup():
    base_path = "%AppData%"
    data_folder = "PythonOS-data"
    setup_file = "setup.txt"
    setup_content = "setup='True'"
    setup_script = "setup.py"
    startup_script = "shell_startup.py"

    # 构建完整路径
    data_path = os.path.join(base_path, data_folder)
    setup_path = os.path.join(data_path, setup_file)
    setup_script_path = os.path.join(setup_script)
    startup_script_path = os.path.join(startup_script)

    # 检查是否存在 PythonOS-data 文件夹
    if not os.path.exists(data_path):
        # 如果不存在，创建文件夹
        os.makedirs(data_path)
        
        # 在 PythonOS-data 文件夹下创建 setup.txt 文件
        with open(setup_path, 'w') as setup_file:
            setup_file.write(setup_content)

        # 执行 setup.py
        os.system(f"python {setup_script_path}")

        # 结束当前 Python 进程
        exit()
    elif not os.path.exists(setup_path):
        # 如果存在 PythonOS-data 文件夹，但没有 setup.txt 文件
        # 创建 setup.txt 文件
        with open(setup_path, 'w') as setup_file:
            setup_file.write(setup_content)

        # 执行 setup.py
        os.system(f"python {setup_script_path}")

        # 结束当前 Python 进程
        exit()
    else:
        # 如果存在 PythonOS-data 文件夹，并且存在 setup.txt 文件，运行 shell_startup.py
        os.system(f"python {startup_script_path}")

if __name__ == "__main__":
    check_and_setup()
