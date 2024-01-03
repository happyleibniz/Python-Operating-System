import pygame
import os
import subprocess
import time

def create_oobe_folder(base_path):
    data_folder = "PythonOS-data"
    oobe_path = os.path.join(base_path, data_folder)

    if not os.path.exists(oobe_path):
        os.makedirs(oobe_path)

def write_account_name(base_path, account_name):
    data_folder = "PythonOS-data"
    account_name_file = "account_name.txt"
    account_name_path = os.path.join(base_path, data_folder, account_name_file)

    with open(account_name_path, 'w') as file:
        file.write(f"account_name={account_name}")

def write_password(base_path, password):
    data_folder = "PythonOS-data"
    password_file = "password.txt"
    password_path = os.path.join(base_path, data_folder, password_file)

    with open(password_path, 'w') as file:
        file.write(f"password={password}")

def install_python_os(base_path):
    # Simulate the installation of PythonOS
    print("Installing PythonOS...")

def run_shell_startup_script():
    shell_startup_script = "shell_startup.py"
    shell_startup_path = os.path.join(shell_startup_script)

    # Check if the shell_startup.py script exists
    if os.path.exists(shell_startup_path):
        # Execute the script in a new process
        subprocess.Popen(["python", shell_startup_script])
    else:
        print(f"Error: {shell_startup_script} not found at {shell_startup_path}!")

def is_mouse_over_button(mouse_pos, button_rect):
    return button_rect.collidepoint(mouse_pos)

def draw_button(screen, text, position, size, color):
    button_rect = pygame.Rect(position, size)
    pygame.draw.rect(screen, color, button_rect, border_radius=10)
    text_render = chinese_font.render(text, True, (255, 255, 255))
    screen.blit(text_render, (position[0] + (size[0] - text_render.get_width()) // 2, position[1] + (size[1] - text_render.get_height()) // 2))

data_folder = "PythonOS-data"

def oobe_screen():
    pygame.init()

    width, height = 1000, 562
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("OOBE")

    clock = pygame.time.Clock()
    running = True
    account_name = ""
    password = ""
    current_step = 0

    chinese_font_path = "font/font3.ttf"
    global chinese_font
    chinese_font = pygame.font.Font(chinese_font_path, 36)

    start_time = pygame.time.get_ticks()

    last_action_time = pygame.time.get_ticks()

    while running:
        current_time = pygame.time.get_ticks()
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()

        # Get all events once per frame
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if current_step == 0:  # Account name setup
                    if event.key == pygame.K_RETURN:
                        current_step += 1
                    elif event.key == pygame.K_BACKSPACE:
                        account_name = account_name[:-1]
                    else:
                        account_name += event.unicode
                elif current_step == 1:  # Password setup
                    if event.key == pygame.K_RETURN:
                        current_step += 1
                        create_oobe_folder(os.path.expanduser("~"))
                        write_account_name(os.path.expanduser("~"), account_name)
                        write_password(os.path.expanduser("~"), password)
                        account_name = ""
                        password = ""
                    elif event.key == pygame.K_BACKSPACE:
                        password = password[:-1]
                    else:
                        password += event.unicode

        screen.fill((255, 255, 255))  # White background

        if current_step == 0:
            text = chinese_font.render(f"请输入您的账户名字： {account_name}", True, (0, 0, 0))
        elif current_step == 1:
            text = chinese_font.render(f"请输入密码： {password}", True, (0, 0, 0))
        else:
            elapsed_time = current_time - start_time
            text = chinese_font.render("正在为你做准备", True, (0, 0, 0))
            text2 = chinese_font.render("请勿关闭PC", True, (128, 0, 0))

            # 显示文字2在经过10秒后
            if elapsed_time >= 20000:
                print("Preparing for installation...")
                install_python_os(os.path.expanduser("~"))
                run_shell_startup_script()
                running = False

        if current_step == 2:
            screen.blit(text2, (width // 2 - text2.get_width() // 2, height // 2 + text.get_height() // 2 + 140))

        screen.blit(text, (width // 2 - text.get_width() // 2, height // 2 - text.get_height() // 2))

        # Render the "Next" button at the bottom right corner
        if current_step < 2:
            button_rect = pygame.Rect(width - 150, height - 50, 2200, 120)  # Increase the button height

            if is_mouse_over_button(mouse_pos, button_rect) and mouse_click[0] and (current_time - last_action_time) > 200:  # Adjust the delay as needed
                print("Button clicked!")
                current_step += 1
                last_action_time = current_time

            if is_mouse_over_button(mouse_pos, button_rect):
                draw_button(screen, "下一步", (width - 160, height - 80), (150, 60), (0, 0, 200))  # Increase the button height
            else:
                draw_button(screen, "下一步", (width - 160, height - 80), (150, 60), (0, 0, 255))  # Increase the button height

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    oobe_screen()
