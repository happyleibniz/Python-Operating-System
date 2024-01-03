import threading
import terminal
terminal_start_get_1=threading.Thread(target=terminal.start_get())
import pygame
import platform
import random
import psutil
from pygame.locals import *
from button import Button
from random import randint
import sys
import easygui as egui
import minecraft
import cv2
import numpy as np
from ffpyplayer.player import MediaPlayer
import webbrowser
pygame.init()
pygame.display.set_caption("PythonOS 1.0.0")
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
def PlayVideo(video_path):

    video=cv2.VideoCapture(video_path)
    player = MediaPlayer(video_path)
    while True:
        grabbed, frame=video.read()
        audio_frame, val = player.get_frame()
        if not grabbed:
            print("End of video")
            break
        if cv2.waitKey(28) & 0xFF == ord("q"):
            break
        cv2.imshow("Video", frame)
        if val != 'eof' and audio_frame is not None:
            #audio
            img, t = audio_frame
    video.release()
    cv2.destroyAllWindows()
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
    link=egui.enterbox("weblink","type the link please")
    if link=="https://www.baidu.com" or link=="https://www.baidu.com/" or link=="www.baidu.com" or link=="baidu.com":
        PlayVideo("./videos/fuck_one.mp4")
        webbrowser.get('windows-default').open(link)
        return
    if link=="https://www.minecraft.net" or link=="https://www.minecraft.net/" or link=="www.minecraft.net" or link=="minecraft.net":
        PlayVideo("./videos/mojang.mp4")
        webbrowser.get('windows-default').open(link)
        return
    webbrowser.get('windows-default').open(link)
def user_defalt():
    global running
    get=False
    running=True
    ggs=False
    viruss=False
    ggss=False
    while running:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        bg_os=pygame.image.load("./images/bg_os.png")
        screen.blit(bg_os,(0,0))

        side_bar=pygame.image.load("./images/sidebar.png")
        side_bar.get_rect()
        screen.blit(side_bar, (0,530))
        start_menu=pygame.image.load("./images/start_menu.png")
        start_menu.get_rect()
        
        close_button_image=pygame.image.load("./images/close.png")
        close_button=Button(image=close_button_image,pos=(5,520),
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
        windows=Button(image=win_image,pos=(25,540),
                     text_input=" ",font=get_font(1),base_color="white",hovering_color="green")
        windows.changeColor(OPTIONS_MOUSE_POS)
        windows.update(screen)
        #chrome image
        chrome_image=pygame.image.load("./images/chrome.png")
        chrome=Button(image=chrome_image,pos=(30,150),
                      text_input="  ",font=get_font(1),base_color="white",hovering_color="green")
        chrome.changeColor(OPTIONS_MOUSE_POS)
        chrome.update(screen)
        mc_logo_image=pygame.image.load("./images/mclogo.png")
        mc=Button(image=mc_logo_image,pos=(30,210),
                  text_input=" ",font=get_font(1),base_color="white",hovering_color="green")
        mc.changeColor(OPTIONS_MOUSE_POS)
        mc.update(screen)
        virus_image=pygame.image.load("./images/virus.png")
        virus=Button(image=virus_image,pos=(30,30),
                     text_input=" ",font=get_font(1),base_color="white",hovering_color="green")
        virus.changeColor(OPTIONS_MOUSE_POS)
        virus.update(screen)
        #########virus things############
        not_found_virus=pygame.image.load("./images/not_find_virus.png")
        not_found_virus.get_rect()
        beat_microsoft_virus=pygame.image.load("./images/beat_microsoft_to_death.png")
        beat_microsoft_virus.get_rect()
        win_script_virus=pygame.image.load("./images/win_script.png")
        win_script_virus.get_rect()
        ms_win_err_virus=pygame.image.load("./images/mswinerr.png")
        ms_win_err_virus.get_rect()
        if viruss==True:
            screen.blit(not_found_virus,(randint(0,1000),randint(0,562)))
            screen.blit(beat_microsoft_virus,(randint(0,1000),randint(0,562)))
            screen.blit(win_script_virus,(randint(0,1000),randint(0,562)))
            screen.blit(ms_win_err_virus,(randint(0,1000),randint(0,562)))
        #virus.end
        recycle_bin_image=pygame.image.load("./images/recycle_bin.png")
        recycle_bin=Button(image=recycle_bin_image,pos=(30,90),
                           text_input=" ",font=get_font(1),base_color="white",hovering_color="green")
        recycle_bin.changeColor(OPTIONS_MOUSE_POS)
        recycle_bin.update(screen)
        
        error_image=pygame.image.load("./images/frame_error.png")
        error_image.get_rect()

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
                    print("virus ahead!")
                    viruss=not viruss
                    print(viruss)
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
                if mc.checkForInput(OPTIONS_MOUSE_POS):
                    print("starting Minecraft")
                    PlayVideo("./videos/intro.mp4")
                    #PlayVideo("./videos/mojang.mp4")
                    
                    #pygame.quit()
                    print("i f**ked pygame :)")
                    #minecraftdd=threading.Thread(target=mc.minecraft.main())
                    #minecraftdd.start()
                    mine_craft=threading.Thread(target=minecraft.main())
                    mine_craft.start()
                    #minecraft.main()
                    

                    
        #return
                    
        pygame.display.update()
def start():
    global running
    get=False
    while running:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill("deepskyblue")

        OPTIONS_TEXT = get_font(15).render("please login", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(600, 30))
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)

        g1=Button(image=None,pos=(150,200),
                  text_input="                 user_free",font=get_font(20),base_color="Black",hovering_color="indigo")
        g1.changeColor(OPTIONS_MOUSE_POS)
        g1.update(screen)
        login=Button(image=None,pos=(350,250),
                     text_input="login",font=get_font(20),base_color="Black",hovering_color="White")
        login.changeColor(OPTIONS_MOUSE_POS)
        login.update(screen)
        #OPTIONS_BACK = Button(image=None, pos=(350, 480), 
        #                    text_input="BACK", font=get_font(20), base_color="Black", hovering_color="Green")

        #OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        #OPTIONS_BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if login.checkForInput(OPTIONS_MOUSE_POS):
                    print("welcome")
                    get=True
                    user_defalt()
                    running=False
                    sys.exit()
                    
        #return
                    
        pygame.display.update()
        if get:
            return
        
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

a=threading.Thread(target=start_computer())
a.start()
