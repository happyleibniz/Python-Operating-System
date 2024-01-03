import threading,multiprocessing
import terminal
terminal_start_get_1=threading.Thread(target=terminal.start_get())
import pygame
import platform
import random
import psutil
import options
from pygame.locals import *
from button import Button
from random import randint
import sys
import easygui as egui
import numpy as np
import os
from datetime import datetime

pygame.init()
pygame.display.set_caption("PythonOS 23H2  2401 build-1.5.2 | © Github-Huangshaoqi,happyleibniz")
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

def BlUe_ScreeN(Error_type):
    global running
    get=False
    while running:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill("blue")

        OPTIONS_TEXT = get_font(15).render("Your computer has encountered an error", True, "White")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(400, 30))
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)

        g1=Button(image=None,pos=(270,50),
                  text_input="self.error."+str(e),font=get_font(10),base_color="White",hovering_color="White")
        g1.changeColor(OPTIONS_MOUSE_POS)
        g1.update(screen)
        g2=Button(image=None,pos=(270,70),
                     text_input="We only collect error information",font=get_font(10),base_color="White",hovering_color="White")
        g2.changeColor(OPTIONS_MOUSE_POS)
        g2.update(screen)
        login=Button(image=None,pos=(210,550),
                     text_input="clickme to shut down :(",font=get_font(20),base_color="Black",hovering_color="White")
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
        
        return   
def chrome_web():
    # creating a pyQt5 application
    app = QApplication(sys.argv)
    
    # setting name to the application
    app.setApplicationName("Browser")
    
    # creating a main window object
    window = MainWindow()
    
    # loop
    app.exec_()


def user_defalt():
    global running
    get=False
    running=True
    ggs=False
    viruss=False
    ggss=False
    font2 = pygame.font.Font("./font/font3.ttf", 13)
    
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
        
        win_image=pygame.image.load("./images/win_button2.png")
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
        """mc_logo_image=pygame.image.load("./images/mclogo.png")
        mc=Button(image=mc_logo_image,pos=(30,210),
                  text_input=" ",font=get_font(1),base_color="white",hovering_color="green")
        mc.changeColor(OPTIONS_MOUSE_POS)
        mc.update(screen)"""

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

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
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
def start():
    global running
    font2 = pygame.font.Font("./font/font3.ttf", 90)
    font3 = pygame.font.Font("./font/font3.ttf", 25)
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

        time_button2 = Button(image=None, pos=(156, 500),
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
    date_str = now.strftime("%Y/%m/%d")
    day_of_week_str = now.strftime("%A")
    return f"{day_of_week_str} {date_str}"

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
try:
    import PyQt5
    from PyQt5.QtCore import *
    from PyQt5.QtWidgets import *
    from PyQt5.QtGui import *
    from PyQt5.QtWebEngineWidgets import *
    from PyQt5.QtPrintSupport import *
    import numpy as np
    #################################################
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
    ###################################

    start_computer()
except Exception as e:
    BlUe_ScreeN(e)
