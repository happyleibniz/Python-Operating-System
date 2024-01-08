import threading
import terminal,subprocess
terminal_start_get_1=threading.Thread(target=terminal.start_get())
import pygame
import platform
import random
#import psutil 这两个库没用，所以注释掉
#import options
from pygame.locals import *
from button import Button
from random import randint
import sys
import easygui as egui
import numpy as np
import os
currentdir=os.getcwd()
from datetime import datetime
import System._config

pygame.init()
pygame.display.set_caption("PythonOS 23H2  2401 build-1.5.3 | © Github-Huangshaoqi,happyleibniz")
vm_info="Pyvm1.0"
booter="Py legends"
os_name = platform.system()
os_version = platform.version()
cpu_info = platform.processor()
ram_info = platform.machine()
WIDTH=1000
HEIGHT=562
is_white=False
if is_white==False:
    bg=pygame.image.load("./images/background_black.png")
    python_os = pygame.image.load('./images/pythonos_white.png')
    # Get the rectangle of the image
    python_os_rect = python_os.get_rect()
    # Set the image coordinates to (0,0)
    
pylegends=pygame.image.load("./images/pylegends2.png")
pylegends_rect=pylegends.get_rect()
pylegends_rect.topleft=(WIDTH/10,HEIGHT/10)

font = pygame.font.Font("./font/font.ttf", 10)
#this is the startup screen
startup=True

os = font.render("vm os:"+str(os_name), True, (255, 255, 255))
os_rect=os.get_rect()
os_rect.topleft=(7,100)
#"os_ver:"+str(os_version)
os_ver = font.render("vm os version:"+str(os_version), True, (255, 255, 255))
osver_rect=os_ver.get_rect()
osver_rect.topleft=(7,115)
#"cpu_info:"+str(cpu_info)
cpu_information = font.render("cpu_info:"+str(cpu_info), True, (255, 255, 255))
cpuinfo_rect=cpu_information.get_rect()
cpuinfo_rect.topleft=(7,130)
#"ram_info:"+str(ram_info)
ram_information = font.render("ram_info:"+str(ram_info), True, (255, 255, 255))
raminfo_rect=ram_information.get_rect()
raminfo_rect.topleft=(7,145)
#"vm version:"+str(vm_info)
vm_ver = font.render("vm version:"+str(vm_info), True, (255, 255, 255))
vm_info_rect=vm_ver.get_rect()
vm_info_rect.topleft=(7,160)
#"booter:"+str(booter)
booter_ver = font.render("booter:"+str(booter), True, (255, 255, 255))
booter_info_rect=vm_ver.get_rect()
booter_info_rect.topleft=(7,175)
#"python version:"+str(py_ver)
python_ver=font.render("python version:"+str(sys.version),True,(255,255,255))
python_ver_rect=python_ver.get_rect()
python_ver_rect.topleft=(7,190)
#loading 1 million modules(not really)
mimodules=font.render("loading 1 M modules--complete",True,(255,255,255))
mimodules_rect=mimodules.get_rect()
mimodules_rect.topleft=(7,205)


screen = pygame.display.set_mode((WIDTH, HEIGHT),RESIZABLE)
running = True
def startproc_mc():
    import subprocess
    pygame.init()
    pygame.display.set_caption("Windows Terminal")

    # Set up fonts
    font = pygame.font.SysFont(None, 24)

    # Set up colors
    white = (255, 255, 255)
    black = (0, 0, 0)

    # Set up variables
    input_text = ""
    output_text = ""

    # Set up variables for scrolling
    scroll_offset = 0
    scroll_speed = 20  # Adjust the scroll speed as needed

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    try:
                        input_text = "pip3 install pyopengl==3.1.5 pyglet==1.5.28 numpy==1.26.1 pygame==2.5.2"
                        output = subprocess.check_output(input_text, shell=True, stderr=subprocess.STDOUT)
                        output_text = output.decode("utf-8")
                        output_text = output_text + "\n"
                    except subprocess.CalledProcessError as e:
                        output_text = e.output.decode("utf-8")
                    input_text = ""
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                elif event.key == pygame.K_UP:
                    scroll_offset += scroll_speed
                elif event.key == pygame.K_DOWN:
                    scroll_offset -= scroll_speed
                else:
                    input_text += event.unicode

        # Clear the screen
        screen.fill(black)

        # Draw the input and output text
        input_surface = font.render("press enter to run" + input_text, True, white)
        screen.blit(input_surface, (10, 10))
        #"press ESC to run minecraft 按ESC运行minecraft"
        input_surface = font.render("press ESC to run minecraft 按ESC运行minecraft" , True, white)

        # Split the output text by the newline character and display each line with scrolling
        output_lines = output_text.split("\n")
        y_position = 40 + scroll_offset
        for line in output_lines:
            output_surface = font.render(line, True, white)
            screen.blit(output_surface, (10, y_position))
            y_position += 20

        # Update the display
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()
    user_defalt()

def BlUe_ScreeN(Error_type):
    global running
    get=False
    while running:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        font0=pygame.font.Font("./font/font3.ttf", 40)
        font1=pygame.font.Font("./font/font3.ttf", 45)
        font2=pygame.font.Font("./font/font3.ttf", 35)
        font3=pygame.font.Font("./font/font3.ttf", 35)
        font4=pygame.font.Font("./font/font3.ttf", 40)
        pygame.init()
        screen.fill("blue")

        OPTIONS_TEXT = font1.render("你的电脑遇到问题", True, "White")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(500, 40))
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)

        g0=Button(image=None,pos=(275,40),
                text_input=":(",font=font0,base_color="White",hovering_color="White")
        g0.changeColor(OPTIONS_MOUSE_POS)
        g0.update(screen)

        g1=Button(image=None,pos=(500,100),
                  text_input="错误代码:"+str(e),font=font2,base_color="White",hovering_color="White")
        g1.changeColor(OPTIONS_MOUSE_POS)
        g1.update(screen)
        g2=Button(image=None,pos=(500,150),
                     text_input="我们只收集错误信息，然后为你重新启动",font=font3,base_color="White",hovering_color="White")
        g2.changeColor(OPTIONS_MOUSE_POS)
        g2.update(screen)
        login=Button(image=None,pos=(210,495),
                     text_input="或者点我关机",font=font4,base_color="White",hovering_color="Gray")
        login.changeColor(OPTIONS_MOUSE_POS)
        login.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if login.checkForInput(OPTIONS_MOUSE_POS):
                    print("shutting down...")
                    pygame.quit()
                    sys.exit()
                    
        pygame.display.update()
        if get:
            return
##################

##################

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("font/font.ttf", size)
def g1():
    global python_os,python_os_rect
    global pylegends, pylegends_rect
    global os,os_rect
    global os_ver,osver_rect
    global cpu_information,cpuinfo_rect
    global ram_information,raminfo_rect
    global vm_ver,vm_info_rect
    global booter_ver,booter_info_rect
    if startup==True:
        screen.blit(python_os, python_os_rect)
        screen.blit(pylegends, pylegends_rect)
        screen.blit(os,os_rect)
        screen.blit(os_ver,osver_rect)
        screen.blit(cpu_information,cpuinfo_rect)
        screen.blit(ram_information,raminfo_rect)
        screen.blit(vm_ver,vm_info_rect)
        screen.blit(booter_ver,booter_info_rect)
        screen.blit(python_ver,python_ver_rect)
        screen.blit(mimodules,mimodules_rect)
        
        
        start2()
def chrome_web():
    # creating main window class
    class MainWindow(QMainWindow):

        # constructor
        def __init__(self, *args, **kwargs):
            super(MainWindow, self).__init__(*args, **kwargs)


            # creating a QWebEngineView
            self.browser = QWebEngineView()

            # setting default browser url as google
            self.browser.setUrl(QUrl("http://www.bing.com"))

            # adding action when url get changed
            self.browser.urlChanged.connect(self.update_urlbar)

            # adding action when loading is finished
            self.browser.loadFinished.connect(self.update_title)

            # set this browser as central widget or main window
            self.setCentralWidget(self.browser)

            # creating a status bar object
            self.status = QStatusBar()

            # adding status bar to the main window
            self.setStatusBar(self.status)

            # creating QToolBar for navigation
            navtb = QToolBar("Navigation")

            # adding this tool bar tot he main window
            self.addToolBar(navtb)

            # adding actions to the tool bar
            # creating a action for back
            back_btn = QAction("Back", self)

            # setting status tip
            back_btn.setStatusTip("Back to previous page")

            # adding action to the back button
            # making browser go back
            back_btn.triggered.connect(self.browser.back)

            # adding this action to tool bar
            navtb.addAction(back_btn)

            # similarly for forward action
            next_btn = QAction("Forward", self)
            next_btn.setStatusTip("Forward to next page")

            # adding action to the next button
            # making browser go forward
            next_btn.triggered.connect(self.browser.forward)
            navtb.addAction(next_btn)

            # similarly for reload action
            reload_btn = QAction("Reload", self)
            reload_btn.setStatusTip("Reload page")

            # adding action to the reload button
            # making browser to reload
            reload_btn.triggered.connect(self.browser.reload)
            navtb.addAction(reload_btn)

            # similarly for home action
            home_btn = QAction("Home", self)
            home_btn.setStatusTip("Go home")
            home_btn.triggered.connect(self.navigate_home)
            navtb.addAction(home_btn)

            # adding a separator in the tool bar
            navtb.addSeparator()

            # creating a line edit for the url
            self.urlbar = QLineEdit()

            # adding action when return key is pressed
            self.urlbar.returnPressed.connect(self.navigate_to_url)

            # adding this to the tool bar
            navtb.addWidget(self.urlbar)

            # adding stop action to the tool bar
            stop_btn = QAction("Stop", self)
            stop_btn.setStatusTip("Stop loading current page")

            # adding action to the stop button
            # making browser to stop
            stop_btn.triggered.connect(self.browser.stop)
            navtb.addAction(stop_btn)

            # showing all the components
            self.show()


        # method for updating the title of the window
        def update_title(self):
            title = self.browser.page().title()
            self.setWindowTitle("% s - Browser" % title)


        # method called by the home action
        def navigate_home(self):

            # open the google
            self.browser.setUrl(QUrl("http://www.baidu.com"))

        # method called by the line edit when return key is pressed
        def navigate_to_url(self):

            # getting url and converting it to QUrl object
            q = QUrl(self.urlbar.text())

            # if url is scheme is blank
            if q.scheme() == "":
                # set url scheme to html
                q.setScheme("http")

            # set the url to the browser
            self.browser.setUrl(q)

        # method for updating url
        # this method is called by the QWebEngineView object
        def update_urlbar(self, q):

            # setting text to the url bar
            self.urlbar.setText(q.toString())

            # setting cursor position of the url bar
            self.urlbar.setCursorPosition(0)
    # creating a pyQt5 application
    app = QApplication(sys.argv)
    
    # setting name to the application
    app.setApplicationName("Browser")
    
    # creating a main window object
    window = MainWindow()
    
    # loop
    app.exec_()


def user_defalt():
    global running,currentdir
    get=False
    running=True
    ggs=False
    viruss=False
    ggss=False
    giig=False
    import pygame
    pygame.display.set_caption("PythonOS 23H2  2401 build-1.5.3 | © Github-Huangshaoqi,happyleibniz")
    pygame.init()
    font2 = pygame.font.Font("./font/font3.ttf", 13)
    bruhhhhh=False
    while running:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        bg_os=pygame.image.load("./images/bg_os3.png")
        screen.blit(bg_os,(0,0))

        side_bar=pygame.image.load("./images/sidebar.png")
        side_bar.get_rect()
        screen.blit(side_bar, (0,530))
        start_menu=pygame.image.load("./images/start_menu.png")
        start_menu.get_rect()
        
        close_button_image=pygame.image.load("./images/ShutDown.png")
        close_button=Button(image=close_button_image,pos=(12,518),
                     text_input=" ",font=get_font(1),base_color="white",hovering_color="green")
        close_button.changeColor(OPTIONS_MOUSE_POS)
        
        if ggs==True:
            start_menu.set_alpha(255)  # Make the surface fully opaque (show it)
            close_button.x_pos=1000
            close_button.y_pos=562
        if ggs==False:
            start_menu.set_alpha(0) 
            close_button.x_pos=5
            close_button.y_pos=520
        screen.blit(start_menu,(0,265))
        close_button.update(screen)
        #start_menu.convert_alpha(255)
        
        win_image=pygame.image.load("./images/win_button.png")
        windows=Button(image=win_image,pos=(25,545),
                     text_input=" ",font=get_font(1),base_color="white",hovering_color="green")
        windows.changeColor(OPTIONS_MOUSE_POS)
        windows.update(screen)
        #serach button(搜索按钮还没有用！！！！！！！！！！！！！！！！)
        searchimg = pygame.image.load("./images/search.png")
        searchbt = Button(image=searchimg,pos=(65,545),
                     text_input=" ",font=get_font(1),base_color="white",hovering_color="green")
        searchbt.changeColor(OPTIONS_MOUSE_POS)
        searchbt.update(screen)
        #edge(chrome) image
        chrome_image=pygame.image.load("./images/Edge2.png")
        chrome=Button(image=chrome_image,pos=(30,160),
                      text_input="  ",font=get_font(1),base_color="white",hovering_color="green")
        chrome.changeColor(OPTIONS_MOUSE_POS)
        chrome.update(screen)
        mc_logo_image=pygame.image.load("./images/mclogo.png")
        mc=Button(image=mc_logo_image,pos=(30,280),
                  text_input=" ",font=get_font(1),base_color="white",hovering_color="green")
        mc.changeColor(OPTIONS_MOUSE_POS)
        mc.update(screen)
        movies=Button(image=pygame.image.load("./images/movie.jpg"),pos=(30,340),
                      text_input="",font=get_font(1),base_color="white",hovering_color="white")
        movies.changeColor(OPTIONS_MOUSE_POS)
        movies.update(screen)

        virus_image=pygame.image.load("./images/computer.png")
        virus=Button(image=virus_image,pos=(30,30),
                     text_input=" ",font=get_font(1),base_color="white",hovering_color="green")
        virus.changeColor(OPTIONS_MOUSE_POS)
        virus.update(screen)

        #Calculator
        Calculatorimg = pygame.image.load("./images/Calculator.png")
        Calculatorbt = Button(Calculatorimg, pos=(30, 225),
                     text_input=" ", font=get_font(1), base_color="white", hovering_color="green")
        Calculatorbt.changeColor(OPTIONS_MOUSE_POS)
        Calculatorbt.update(screen)

        recycle_bin_image=pygame.image.load("./images/Recycle0.png")
        recycle_bin=Button(image=recycle_bin_image,pos=(30,90),
                           text_input=" ",font=get_font(1),base_color="white",hovering_color="green")
        recycle_bin.changeColor(OPTIONS_MOUSE_POS)
        recycle_bin.update(screen)
        
        error_image=pygame.image.load("./images/frame_error.png")
        error_image.get_rect()

        time_button = Button(image=None, pos=(950, 537.5),
                             text_input=get_desktop_time(), font=font2, base_color="White", hovering_color="White")
        time_button.changeColor(OPTIONS_MOUSE_POS)
        time_button.update(screen)
        time_button2=Button(image=None, pos=(950, 552),
                             text_input=get_desktop_time2(), font=font2, base_color="White", hovering_color="White")
        time_button2.changeColor(OPTIONS_MOUSE_POS)
        time_button2.update(screen)

        if ggss==True:
            error_image.set_alpha(255)  # Make the surface fully opaque (show it)

        if ggss==False:
            error_image.set_alpha(0) 
        screen.blit(error_image,(250,190))
        #screen.blit(recycle_bin,(10,80))
        #OPTIONS_BACK = Button(image=None, pos=(350, 480), 
        #                    text_input="BACK", font=get_font(20), base_color="Black", hovering_color="Green")

        #OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        #OPTIONS_BACK.update(screen)
        try:
            video_excample.draw_to(screen, (100, 50))
        except:
            pass
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if bruhhhhh==True:
                        if giig==False:
                            giig=True
                            print("huh")
                            video_excample.stop()
                        elif giig==True:
                            video_excample.play()
                if event.key == pygame.K_q:
                    if bruhhhhh==True:
                        video_excample.stop()
                        video_excample=None
                        pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if movies.checkForInput(OPTIONS_MOUSE_POS):
                    bruhhhhh=True
                    if bruhhhhh==True:
                        from software.vid_player.vid_player import Video

                        video_excample = Video("video.mkv")#you can use .mp4
                        video_excample.play()
                        #bruhhhhh=False
                    elif bruhhhhh==False:
                        pass
                if mc.checkForInput(OPTIONS_MOUSE_POS):
                    subprocess.check_output("pip3 install pyopengl==3.1.5 pyglet==1.5.28 numpy==1.26.1 pygame==2.5.2")
                    print("loading metadata...")
                    #__glkd=currentdir+'\\minecraft_python_editon'

                    #sys.path.append(__glkd)
                    #print(sys.path)
                    import minecraft_python_edition.minecraft
                if windows.checkForInput(OPTIONS_MOUSE_POS):
                    print("start menu")
                    ggs=not ggs
                    print(ggs)
                if virus.checkForInput(OPTIONS_MOUSE_POS):
                    import os
                    os.system("python software/code/This-PC.py")
                    print("Open PC")
                if recycle_bin.checkForInput(OPTIONS_MOUSE_POS):
                    print("recycle bin selected")
                    ggss=not ggss
                    print(ggss)
                if close_button.checkForInput(OPTIONS_MOUSE_POS):
                    print("closed:)")
                    pygame.quit()
                    sys.exit()
                if chrome.checkForInput(OPTIONS_MOUSE_POS):
                    print("clicked on chrome")
                    print("starting chrome")
                    chorme_start=threading.Thread(target=chrome_web())
                if Calculatorbt.checkForInput(OPTIONS_MOUSE_POS):
                    import os
                    os.system("start software/Calculator.exe")
                    print("cala")
                    
        pygame.display.update()

def start2():
    global running, bg_install
    get = False
    startuplist=[]
    
    for i in range(1,90):
        startuplist.append(pygame.image.load(f"./images/startup/startup_{i}.png"))
        print(startuplist)
    crraima=0

    screen.fill((0, 0, 0))
    #windows logo
    windows_leftup=pygame.image.load("./images/win1.png")
    windows_rightup=pygame.image.load("./images/win2.png")
    windows_leftdown=pygame.image.load("./images/win3.png")
    windows_rightdown=pygame.image.load("./images/win4.png")
    clock = pygame.time.Clock()
    for i in range(100):
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        screen.blit(windows_leftup,(364,54)) #305,15
        screen.blit(windows_rightup,(499,54)) #440,15
        screen.blit(windows_leftdown,(364,189)) #314,154
        screen.blit(windows_rightdown,(499,189)) #449,153
        screen.blit(startuplist[crraima], (430, 400)) #370
        pygame.display.flip()
        clock.tick(25)
        crraima = (crraima + 1) % len(startuplist)

 
                    
        pygame.display.update()
    start()

def start():
    global running
    font2 = pygame.font.Font("./font/font3.ttf", 90)
    font3 = pygame.font.Font("./font/font3.ttf", 28)
    font4 = pygame.font.Font("./font/font3.ttf", 23)
    get = False
    while running:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill((0, 122, 204))
        #screen.fill("deepskyblue")

        time_button = Button(image=None, pos=(150, 430),
                             text_input=get_current_time(), font=font2, base_color="White", hovering_color="White")
        time_button.changeColor(OPTIONS_MOUSE_POS)
        time_button.update(screen)

        time_button2 = Button(image=None, pos=(157, 500),
                              text_input=get_current_time2(), font=font3, base_color="White", hovering_color="White")
        time_button2.changeColor(OPTIONS_MOUSE_POS)
        time_button2.update(screen)

        login = Button(image=None, pos=(930, 520),
                       text_input="登录", font=font4, base_color="White", hovering_color="Gray")
        login.changeColor(OPTIONS_MOUSE_POS)
        login.update(screen)
        account_img=pygame.image.load("./images/account2.png")
        account_bt=Button(image=account_img,pos=(930,473),
                           text_input=" ",font=get_font(1),base_color="white",hovering_color="green")
        account_bt.changeColor(OPTIONS_MOUSE_POS)
        account_bt.update(screen)

        wuzaiimg=pygame.image.load("./images/wuzhangai.png")
        wuzaibt=Button(image=wuzaiimg,pos=(872,521),
                           text_input=" ",font=get_font(1),base_color="white",hovering_color="green")
        wuzaibt.changeColor(OPTIONS_MOUSE_POS)
        wuzaibt.update(screen)
        msimg=pygame.image.load("./images/Microsoft2.png")
        msbt=Button(image=msimg,pos=(930,30),
                           text_input=" ",font=get_font(1),base_color="white",hovering_color="green")
        msbt.changeColor(OPTIONS_MOUSE_POS)
        msbt.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if login.checkForInput(OPTIONS_MOUSE_POS):
                    print("welcome")
                    get = True
                    user_defalt()
                    running = False
                    sys.exit()

        pygame.display.update()
        if get:
            return


def get_current_time():
    now = datetime.now()
    time_str = now.strftime("%H:%M")
    return f"{time_str}"

def get_current_time2():
    now = datetime.now()
    
    # 映射英文星期到中文星期
    day_of_week_mapping = {
        'Monday': '星期一',
        'Tuesday': '星期二',
        'Wednesday': '星期三',
        'Thursday': '星期四',
        'Friday': '星期五',
        'Saturday': '星期六',
        'Sunday': '星期日',  # 将星期日映射为星期一
    }

    date_str = now.strftime("%Y/%m/%d")
    day_of_week_str = now.strftime("%A")
    
    # 获取中文星期
    chinese_day_of_week = day_of_week_mapping.get(day_of_week_str, day_of_week_str)

    return f"{chinese_day_of_week} {date_str}"

def get_desktop_time():
    now = datetime.now()
    time_str = now.strftime("%H:%M:%S")
    return f"{time_str}"

def get_desktop_time2():
    now = datetime.now()
    date_str = now.strftime("%Y/%m/%d")
    return f"{date_str}"

gg=0
def start_computer():
    global b,gg
    global running,is_white
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                # Quit Pygame
                pygame.quit()
                sys.exit()
                

        # Update game logic

        # Draw graphics
        pygame.display.flip()
        screen.fill((0,0,0))
        screen.blit(bg,(0,0))
        # Blit the image onto the screen
        if is_white==False:
            python_os_rect.topleft = (WIDTH/2/1.2, 0)
        g1()
        #python_os,pylegends,os,os_ver,cpu_information,ram_information,vm_ver,booter_ver.set_alpha(0)#0 is fully trans and 255 is unfully trans
        
        #for i in range(1000000000):
        #    gg+=1
        if gg>=10000:
            start()
            sys.exit()
        gg+=1
        
    return

import PyQt5
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *
import numpy as np
#################################################

###################################

start_computer()
#except Exception as e:
#    BlUe_ScreeN(e)
