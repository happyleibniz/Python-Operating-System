import pygame,time
import sys,platform
from pygame.locals import *
from button import Button 
from PIL import Image, ImageSequence
import pygame.image
import os

pygame.init()
pygame.display.set_caption("PythonOS 安装程序")
vm_info="Pyvm1.1"
booter="Py legends"
os_name = platform.system()
os_version = platform.version()
cpu_info = platform.processor()
ram_info = platform.machine()
WIDTH=1000
HEIGHT=562
bg_install=pygame.image.load("./running logo/background.png")
is_white=False
if is_white==False:
    bg=pygame.image.load("./images/background_black.png")
    python_os = pygame.image.load('./images/pythonos_white.png')
    python_os_rect = python_os.get_rect()
    
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
def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("font/font.ttf", size)
def get_calibri_font(size):
    return pygame.font.Font("font/calibri.ttf",size)
def get_hanzi_font(size):
    return pygame.font.Font("font/usehanzi.ttf",size)
def get_hanzijianti_font(size):
    return pygame.font.Font("font/jianti (1).ttc",size)
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
def restart_2():
    global running, bg_install
    get = False
    startuplist=[]
    
    for i in range(1,90):
        startuplist.append(pygame.image.load(f"./images/startup/startup_{i}.png"))
        print(startuplist)
    crraima=0

    screen.fill((0, 0, 0))
    #windows logo
    windows_leftup=pygame.image.load("./running logo/win1.png")
    windows_rightup=pygame.image.load("./running logo/win2.png")
    windows_leftdown=pygame.image.load("./running logo/win3.png")
    windows_rightdown=pygame.image.load("./running logo/win4.png")
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
def hman_next():
    global running,bg_install   
    get=False
    globe=pygame.image.load("./running logo/human.svg")
    g1=Button(image=pygame.image.load("./running logo/global white un select.png"),pos=(350,200),
                  text_input="                 自动设置",font=get_hanzijianti_font(20),base_color="Black",hovering_color="Black")
    networking=Button(image=pygame.image.load("./running logo/networkgood.png"),pos=(300,200),text_input="",font=get_font(0),base_color="black",hovering_color="black")
    
    while running:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        #screen.fill("cyan")

        screen.fill("black")
        screen.blit(bg_install,(0,0))
        OPTIONS_TEXT = get_hanzijianti_font(35).render("如何设置？", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(500, 30))
        networking.changeColor(OPTIONS_MOUSE_POS)
        networking.update(screen)

        system_choose=Button(image=pygame.image.load("./running logo/system choose white.png"),pos=(500,281),text_input="",font=get_font(0),base_color="black",hovering_color="black")
        system_choose.changeColor(OPTIONS_MOUSE_POS)
        system_choose.update(screen)
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)
        
        g1.changeColor(OPTIONS_MOUSE_POS)
        g1.update(screen)       
        next=Button(image=pygame.image.load("./running logo/next_button.png"),pos=(800,450),
                     text_input="下一步",font=get_hanzijianti_font(30),base_color="Black",hovering_color="White")
        next.changeColor(OPTIONS_MOUSE_POS)
        next.update(screen)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if g1.checkForInput(OPTIONS_MOUSE_POS):
                    g1.image=pygame.image.load("./running logo/global white selected.png")
                if next.checkForInput(OPTIONS_MOUSE_POS):
                    #restart_2()
                    import os
                    os.system("python shell_startup.py")
                    pygame.quit()
                    
        #return
                    
        pygame.display.update()
        if get:
            return
def hmanask():
    global running, bg_install
    get = False
    startuplist=[]
    
    for i in range(1,35):
        startuplist.append(pygame.image.load(f"./images/startupv/startupv_{i}.png"))
        print(startuplist)
    crraima=0

    
    globe=pygame.image.load("./running logo/human.svg")
    clock = pygame.time.Clock()
    for i in range(100):
        screen.fill((0, 0, 0))
        screen.blit(bg_install,(0,0))
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        screen.blit(globe,(100,100))
        screen.blit(startuplist[crraima], (370, 200))
        pygame.display.flip()
        clock.tick(25)
        crraima = (crraima + 1) % len(startuplist)
    
                    
        pygame.display.update()
    hman_next()
def wifi_next():
    global running,bg_install   
    get=False
    globe=pygame.image.load("./running logo/network.svg")
    g1=Button(image=pygame.image.load("./running logo/global white un select.png"),pos=(350,200),
                  text_input="                 以太网",font=get_hanzijianti_font(20),base_color="Black",hovering_color="Black")
    networking=Button(image=pygame.image.load("./running logo/networkgood.png"),pos=(300,200),text_input="",font=get_font(0),base_color="black",hovering_color="black")
    
    while running:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        #screen.fill("cyan")

        screen.fill("black")
        screen.blit(bg_install,(0,0))
        OPTIONS_TEXT = get_hanzijianti_font(25).render("让我们为你连接网络", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(300, 30))
        networking.changeColor(OPTIONS_MOUSE_POS)
        networking.update(screen)

        system_choose=Button(image=pygame.image.load("./running logo/system choose white.png"),pos=(500,281),text_input="",font=get_font(0),base_color="black",hovering_color="black")
        system_choose.changeColor(OPTIONS_MOUSE_POS)
        system_choose.update(screen)
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)
        
        g1.changeColor(OPTIONS_MOUSE_POS)
        g1.update(screen)      
        next=Button(image=pygame.image.load("./running logo/next_button.png"),pos=(800,450),
                     text_input="下一步",font=get_hanzijianti_font(30),base_color="Black",hovering_color="White")
        next.changeColor(OPTIONS_MOUSE_POS)
        next.update(screen)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if g1.checkForInput(OPTIONS_MOUSE_POS):
                    g1.image=pygame.image.load("./running logo/global white selected.png")
                if next.checkForInput(OPTIONS_MOUSE_POS):
                    hmanask()
                    
        #return
                    
        pygame.display.update()
        if get:
            return
def wifiask():
    global running, bg_install
    get = False
    startuplist=[]
    
    for i in range(1,35):
        startuplist.append(pygame.image.load(f"./images/startupv/startupv_{i}.png"))
        print(startuplist)
    crraima=0

    
    globe=pygame.image.load("./running logo/network.svg")
    clock = pygame.time.Clock()
    for i in range(100):
        screen.fill((0, 0, 0))
        screen.blit(bg_install,(0,0))
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        screen.blit(globe,(100,100))
        screen.blit(startuplist[crraima], (370, 200))
        pygame.display.flip()
        clock.tick(25)
        crraima = (crraima + 1) % len(startuplist)
    
                    
        pygame.display.update()
    wifi_next()
def keyboard_next():
    global running,bg_install   
    get=False
    globe=pygame.image.load("./running logo/keyboard.svg")
    g1=Button(image=pygame.image.load("./running logo/global white un select.png"),pos=(350,200),
                  text_input="微软拼音输入法/ENG/微软五笔输入法",font=get_hanzijianti_font(20),base_color="Black",hovering_color="Black")
    while running:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        #screen.fill("cyan")

        screen.fill("black")
        screen.blit(bg_install,(0,0))
        OPTIONS_TEXT = get_hanzijianti_font(25).render("请选择键盘格式：", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(300, 30))

        system_choose=Button(image=pygame.image.load("./running logo/system choose white.png"),pos=(500,281),text_input="",font=get_font(0),base_color="black",hovering_color="black")
        system_choose.changeColor(OPTIONS_MOUSE_POS)
        system_choose.update(screen)
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)
        
        g1.changeColor(OPTIONS_MOUSE_POS)
        g1.update(screen)     
        next=Button(image=pygame.image.load("./running logo/next_button.png"),pos=(800,450),
                     text_input="下一步",font=get_hanzijianti_font(30),base_color="Black",hovering_color="White")
        next.changeColor(OPTIONS_MOUSE_POS)
        next.update(screen)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if g1.checkForInput(OPTIONS_MOUSE_POS):
                    g1.image=pygame.image.load("./running logo/global white selected.png")
                if next.checkForInput(OPTIONS_MOUSE_POS):
                    wifiask()
                    
        #return
                    
        pygame.display.update()
        if get:
            return
def keyboardask():
    global running, bg_install
    get = False
    startuplist=[]
    
    for i in range(1,35):
        startuplist.append(pygame.image.load(f"./images/startupv/startupv_{i}.png"))
        print(startuplist)
    crraima=0

    
    globe=pygame.image.load("./running logo/keyboard.svg")
    clock = pygame.time.Clock()
    for i in range(100):
        screen.fill((0, 0, 0))
        screen.blit(bg_install,(0,0))
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        screen.blit(globe,(100,100))
        screen.blit(startuplist[crraima], (370, 200))
        pygame.display.flip()
        clock.tick(25)
        crraima = (crraima + 1) % len(startuplist)
    
                    
        pygame.display.update()
    keyboard_next()
def asking_next():
    global running,bg_install   
    get=False
    globe=pygame.image.load("./running logo/globe.svg")
    g1=Button(image=pygame.image.load("./running logo/global white un select.png"),pos=(340,215),
                  text_input="           中国大陆",font=get_hanzijianti_font(20),base_color="Black",hovering_color="Black")
    g2=Button(image=pygame.image.load("./running logo/global white un select.png"),pos=(660,215),
                text_input="             中国台湾",font=get_hanzijianti_font(20),base_color="Black",hovering_color="Black")
    g3=Button(image=pygame.image.load("./running logo/global white un select.png"),pos=(340,280),
                text_input="             中国香港",font=get_hanzijianti_font(20),base_color="Black",hovering_color="Black")
    g4=Button(image=pygame.image.load("./running logo/global white un select.png"),pos=(660,280),
                text_input="             中国澳门",font=get_hanzijianti_font(20),base_color="Black",hovering_color="Black")  
    while running:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        #screen.fill("cyan")

        screen.fill("black")
        screen.blit(bg_install,(0,0))
        OPTIONS_TEXT = get_hanzijianti_font(25).render("请选择您所在的国家：", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(300, 30))

        system_choose=Button(image=pygame.image.load("./running logo/system choose white.png"),pos=(500,281),text_input="",font=get_font(0),base_color="black",hovering_color="black")
        system_choose.changeColor(OPTIONS_MOUSE_POS)
        system_choose.update(screen)
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)
        
        g1.changeColor(OPTIONS_MOUSE_POS)
        g1.update(screen)
        g2.changeColor(OPTIONS_MOUSE_POS)
        g2.update(screen)
        g3.changeColor(OPTIONS_MOUSE_POS)
        g3.update(screen)
        g4.changeColor(OPTIONS_MOUSE_POS)
        g4.update(screen)
        next=Button(image=pygame.image.load("./running logo/next_button.png"),pos=(800,450),
                     text_input="下一步",font=get_hanzijianti_font(30),base_color="Black",hovering_color="White")
        next.changeColor(OPTIONS_MOUSE_POS)
        next.update(screen)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if g1.checkForInput(OPTIONS_MOUSE_POS):
                    g1.image=pygame.image.load("./running logo/global white selected.png")
                if g2.checkForInput(OPTIONS_MOUSE_POS):
                    g2.image=pygame.image.load("./running logo/global white selected.png")
                if g3.checkForInput(OPTIONS_MOUSE_POS):
                    g3.image=pygame.image.load("./running logo/global white selected.png")
                if g4.checkForInput(OPTIONS_MOUSE_POS):
                    g4.image=pygame.image.load("./running logo/global white selected.png")
                if next.checkForInput(OPTIONS_MOUSE_POS):
                    keyboardask()
                    
        #return
                    
        pygame.display.update()
        if get:
            return
def asking():
    global running, bg_install
    get = False
    startuplist=[]
    
    for i in range(1,35):
        startuplist.append(pygame.image.load(f"./images/startupv/startupv_{i}.png"))
        print(startuplist)
    crraima=0

    
    globe=pygame.image.load("./running logo/globe.svg")
    clock = pygame.time.Clock()
    for i in range(100):
        screen.fill((0, 0, 0))
        screen.blit(bg_install,(0,0))
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        screen.blit(globe,(100,100))
        screen.blit(startuplist[crraima], (370, 200))
        pygame.display.flip()
        clock.tick(25)
        crraima = (crraima + 1) % len(startuplist)
    
                    
        pygame.display.update()
    asking_next()
def restart():
    global running, bg_install
    get = False
    startuplist=[]
    
    for i in range(1,90):
        startuplist.append(pygame.image.load(f"./images/startup/startup_{i}.png"))
        print(startuplist)
    crraima=0

    screen.fill((0, 0, 0))
    #windows logo
    windows_leftup=pygame.image.load("./running logo/win1.png")
    windows_rightup=pygame.image.load("./running logo/win2.png")
    windows_leftdown=pygame.image.load("./running logo/win3.png")
    windows_rightdown=pygame.image.load("./running logo/win4.png")
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
    asking()
def finishing_installation():
    global running,bg_install   
    get=False
    while running:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        #screen.fill("cyan")

        screen.fill("black")
        screen.blit(bg_install,(0,0))
        ins_image=pygame.image.load("./running logo/setup-icon.png")
        insbt=Button(image=ins_image,pos=(30,30),
                     text_input=" ",font=get_font(1),base_color="white",hovering_color="white")
        insbt.changeColor(OPTIONS_MOUSE_POS)
        insbt.update(screen)
        OPTIONS_TEXT = get_hanzijianti_font(25).render("PythonOS安装程序", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(170, 30))

        system_choose=Button(image=pygame.image.load("./running logo/system choose white.png"),pos=(500,281),text_input="",font=get_font(0),base_color="black",hovering_color="black")
        system_choose.changeColor(OPTIONS_MOUSE_POS)
        system_choose.update(screen)
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)
        g1=Button(image=None,pos=(300,200),
                  text_input="                 安装已完成，请重启。",font=get_hanzijianti_font(20),base_color="Black",hovering_color="Black")
        g1.changeColor(OPTIONS_MOUSE_POS)
        g1.update(screen)
        copyright=Button(image=None,pos=(160,510),
                  text_input="© Github-Huangshaoqi 2023",font=get_hanzijianti_font(20),base_color="Black",hovering_color="black")
        copyright.changeColor(OPTIONS_MOUSE_POS)
        copyright.update(screen)
        copyright2=Button(image=None,pos=(120,535),
                  text_input="© happyleibniz 2023",font=get_hanzijianti_font(20),base_color="Black",hovering_color="black")
        copyright2.changeColor(OPTIONS_MOUSE_POS)
        copyright2.update(screen)        
        next=Button(image=pygame.image.load("./running logo/next_button.png"),pos=(800,450),
                     text_input="重启",font=get_hanzijianti_font(30),base_color="Black",hovering_color="White")
        next.changeColor(OPTIONS_MOUSE_POS)
        next.update(screen)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if next.checkForInput(OPTIONS_MOUSE_POS):
                    restart()
                    
        #return
                    
        pygame.display.update()
        if get:
            return
def compressfileproc():
    global running,bg_install,max_value,value
    get=False
    #progress_color = (0, 0, 255) # blue
    max_value = 100
    value = 0  
    while running:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        #screen.fill("cyan")

        screen.fill("black")
        screen.blit(bg_install,(0,0))
        OPTIONS_TEXT = get_hanzijianti_font(25).render("安装程序正在压缩文件，请稍后...", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(550, 30))
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)
        #ji ni tai mei~~~~~~~~~~~~~~~!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!~~~~~~~~~~~~~~~~~~~~
        draw_progress_bar(value)
        if value!=34.900000000000226:
            value += 0.1
        else:
            finishing_installation()
def compressfile():
    global running,bg_install   
    get=False
    while running:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        #screen.fill("cyan")

        screen.fill("black")
        screen.blit(bg_install,(0,0))
        ins_image=pygame.image.load("./running logo/setup-icon.png")
        insbt=Button(image=ins_image,pos=(30,30),
                     text_input=" ",font=get_font(1),base_color="white",hovering_color="white")
        insbt.changeColor(OPTIONS_MOUSE_POS)
        insbt.update(screen)
        OPTIONS_TEXT = get_hanzijianti_font(25).render("PythonOS安装程序", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(170, 30))

        system_choose=Button(image=pygame.image.load("./running logo/system choose white.png"),pos=(500,281),text_input="",font=get_font(0),base_color="black",hovering_color="black")
        system_choose.changeColor(OPTIONS_MOUSE_POS)
        system_choose.update(screen)
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)
        g1=Button(image=None,pos=(300,200),
                  text_input="                 安装程序正在压缩文件，请稍后...",font=get_hanzijianti_font(20),base_color="Black",hovering_color="Black")
        g1.changeColor(OPTIONS_MOUSE_POS)
        g1.update(screen)
        copyright=Button(image=None,pos=(160,510),
                  text_input="© Github-Huangshaoqi 2023",font=get_hanzijianti_font(20),base_color="Black",hovering_color="black")
        copyright.changeColor(OPTIONS_MOUSE_POS)
        copyright.update(screen)
        copyright2=Button(image=None,pos=(120,535),
                  text_input="© happyleibniz 2023",font=get_hanzijianti_font(20),base_color="Black",hovering_color="black")
        copyright2.changeColor(OPTIONS_MOUSE_POS)
        copyright2.update(screen)        
        img_image=pygame.image.load("./running logo/folder.png")
        imgbt=Button(image=img_image,pos=(270,300),
                     text_input=" ",font=get_font(1),base_color="white",hovering_color="white")
        imgbt.changeColor(OPTIONS_MOUSE_POS)
        imgbt.update(screen)
        next=Button(image=pygame.image.load("./running logo/next_button.png"),pos=(800,450),
                     text_input="确定",font=get_hanzijianti_font(30),base_color="Black",hovering_color="White")
        next.changeColor(OPTIONS_MOUSE_POS)
        next.update(screen)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if next.checkForInput(OPTIONS_MOUSE_POS):
                    compressfileproc()
                    
        #return
                    
        pygame.display.update()
        if get:
            return
def gettingiso():
    global running,bg_install,max_value,value
    get=False
    #progress_color = (0, 0, 255) # blue
    max_value = 100
    value = 0  
    while running:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        #screen.fill("cyan")

        screen.fill("black")
        screen.blit(bg_install,(0,0))
        OPTIONS_TEXT = get_hanzijianti_font(25).render("安装程序正在准备镜像，请稍后...", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(550, 30))
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)
        #ji ni tai mei~~~~~~~~~~~~~~~!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!~~~~~~~~~~~~~~~~~~~~
        draw_progress_bar(value)
        if value!=12:
            value += 1
        else:
            compressfile()
def prepareiso():
    #准备镜像
    global running,bg_install   
    get=False
    while running:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        #screen.fill("cyan")

        screen.fill("black")
        screen.blit(bg_install,(0,0))
        ins_image=pygame.image.load("./running logo/setup-icon.png")
        insbt=Button(image=ins_image,pos=(30,30),
                     text_input=" ",font=get_font(1),base_color="white",hovering_color="white")
        insbt.changeColor(OPTIONS_MOUSE_POS)
        insbt.update(screen)
        OPTIONS_TEXT = get_hanzijianti_font(25).render("PythonOS安装程序", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(170, 30))

        system_choose=Button(image=pygame.image.load("./running logo/system choose white.png"),pos=(500,281),text_input="",font=get_font(0),base_color="black",hovering_color="black")
        system_choose.changeColor(OPTIONS_MOUSE_POS)
        system_choose.update(screen)
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)
        g1=Button(image=None,pos=(300,200),
                  text_input="                 安装程序正在准备镜像，请稍后...",font=get_hanzijianti_font(20),base_color="Black",hovering_color="Black")
        g1.changeColor(OPTIONS_MOUSE_POS)
        g1.update(screen)
        copyright=Button(image=None,pos=(160,510),
                  text_input="© Github-Huangshaoqi 2023",font=get_hanzijianti_font(20),base_color="Black",hovering_color="black")
        copyright.changeColor(OPTIONS_MOUSE_POS)
        copyright.update(screen)
        copyright2=Button(image=None,pos=(120,535),
                  text_input="© happyleibniz 2023",font=get_hanzijianti_font(20),base_color="Black",hovering_color="black")
        copyright2.changeColor(OPTIONS_MOUSE_POS)
        copyright2.update(screen)        
        img_image=pygame.image.load("./running logo/folder-box.png")
        imgbt=Button(image=img_image,pos=(270,300),
                     text_input=" ",font=get_font(1),base_color="white",hovering_color="white")
        imgbt.changeColor(OPTIONS_MOUSE_POS)
        imgbt.update(screen)
        next=Button(image=pygame.image.load("./running logo/next_button.png"),pos=(800,450),
                     text_input="确定",font=get_hanzijianti_font(30),base_color="Black",hovering_color="White")
        next.changeColor(OPTIONS_MOUSE_POS)
        next.update(screen)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if next.checkForInput(OPTIONS_MOUSE_POS):
                    gettingiso()
                    
        #return
                    
        pygame.display.update()
        if get:
            return
def delfileproc():
    global running,bg_install,max_value,value
    get=False
    #progress_color = (0, 0, 255) # blue
    max_value = 100
    value = 0  
    while running:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        #screen.fill("cyan")

        screen.fill("black")
        screen.blit(bg_install,(0,0))
        OPTIONS_TEXT = get_hanzijianti_font(25).render("安装程序正在删除文件，请稍后...", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(550, 30))
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)
        #ji ni tai mei~~~~~~~~~~~~~~~!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!~~~~~~~~~~~~~~~~~~~~
        draw_progress_bar(value)
        if value!=34.900000000000226:
            value += 0.1
        else:
            prepareiso()
def delfile():
    #删除文件
    global running,bg_install   
    get=False
    while running:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        #screen.fill("cyan")

        screen.fill("black")
        screen.blit(bg_install,(0,0))
        ins_image=pygame.image.load("./running logo/setup-icon.png")
        insbt=Button(image=ins_image,pos=(30,30),
                     text_input=" ",font=get_font(1),base_color="white",hovering_color="white")
        insbt.changeColor(OPTIONS_MOUSE_POS)
        insbt.update(screen)
        OPTIONS_TEXT = get_hanzijianti_font(25).render("PythonOS安装程序", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(170, 30))

        system_choose=Button(image=pygame.image.load("./running logo/system choose white.png"),pos=(500,281),text_input="",font=get_font(0),base_color="black",hovering_color="black")
        system_choose.changeColor(OPTIONS_MOUSE_POS)
        system_choose.update(screen)
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)
        g1=Button(image=None,pos=(300,200),
                  text_input="                 安装程序正在删除旧文件，请稍后...",font=get_hanzijianti_font(20),base_color="Black",hovering_color="Black")
        g1.changeColor(OPTIONS_MOUSE_POS)
        g1.update(screen)
        copyright=Button(image=None,pos=(160,510),
                  text_input="© Github-Huangshaoqi 2023",font=get_hanzijianti_font(20),base_color="Black",hovering_color="black")
        copyright.changeColor(OPTIONS_MOUSE_POS)
        copyright.update(screen)
        copyright2=Button(image=None,pos=(120,535),
                  text_input="© happyleibniz 2023",font=get_hanzijianti_font(20),base_color="Black",hovering_color="black")
        copyright2.changeColor(OPTIONS_MOUSE_POS)
        copyright2.update(screen)        
        img_image=pygame.image.load("./running logo/flie.png")
        imgbt=Button(image=img_image,pos=(270,300),
                     text_input=" ",font=get_font(1),base_color="white",hovering_color="white")
        imgbt.changeColor(OPTIONS_MOUSE_POS)
        imgbt.update(screen)
        next=Button(image=pygame.image.load("./running logo/next_button.png"),pos=(800,450),
                     text_input="确定",font=get_hanzijianti_font(30),base_color="Black",hovering_color="White")
        next.changeColor(OPTIONS_MOUSE_POS)
        next.update(screen)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if next.checkForInput(OPTIONS_MOUSE_POS):
                    delfileproc()
                    
        #return
                    
        pygame.display.update()
        if get:
            return
def checkdisk():
    global running,bg_install,max_value,value
    get=False
    #progress_color = (0, 0, 255) # blue
    max_value = 100
    value = 0  
    while running:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        #screen.fill("cyan")

        screen.fill("black")
        screen.blit(bg_install,(0,0))
        OPTIONS_TEXT = get_hanzijianti_font(25).render("安装程序正在检查硬盘，请稍后...", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(550, 30))
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)

        draw_progress_bar(value)
        if value!=12: #34.900000000000226
            value += 1 #0.1
        else:
            delfile()
def install():
    global running,bg_install   
    get=False
    while running:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        #screen.fill("cyan")

        screen.fill("black")
        screen.blit(bg_install,(0,0))
        ins_image=pygame.image.load("./running logo/setup-icon.png")
        insbt=Button(image=ins_image,pos=(30,30),
                     text_input=" ",font=get_font(1),base_color="white",hovering_color="white")
        insbt.changeColor(OPTIONS_MOUSE_POS)
        insbt.update(screen)
        OPTIONS_TEXT = get_hanzijianti_font(25).render("PythonOS安装程序", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(170, 30))

        system_choose=Button(image=pygame.image.load("./running logo/system choose white.png"),pos=(500,281),text_input="",font=get_font(0),base_color="black",hovering_color="black")
        system_choose.changeColor(OPTIONS_MOUSE_POS)
        system_choose.update(screen)
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)
        g1=Button(image=None,pos=(300,200),
                  text_input="                 安装程序正在检查硬盘，请稍后...",font=get_hanzijianti_font(20),base_color="Black",hovering_color="Black")
        g1.changeColor(OPTIONS_MOUSE_POS)
        g1.update(screen)
        copyright=Button(image=None,pos=(160,510),
                  text_input="© Github-Huangshaoqi 2023",font=get_hanzijianti_font(20),base_color="Black",hovering_color="black")
        copyright.changeColor(OPTIONS_MOUSE_POS)
        copyright.update(screen)
        copyright2=Button(image=None,pos=(120,535),
                  text_input="© happyleibniz 2023",font=get_hanzijianti_font(20),base_color="Black",hovering_color="black")
        copyright2.changeColor(OPTIONS_MOUSE_POS)
        copyright2.update(screen)        
        img_image=pygame.image.load("./running logo/Disk2.png")
        imgbt=Button(image=img_image,pos=(270,300),
                     text_input=" ",font=get_font(1),base_color="white",hovering_color="white")
        imgbt.changeColor(OPTIONS_MOUSE_POS)
        imgbt.update(screen)
        next=Button(image=pygame.image.load("./running logo/next_button.png"),pos=(800,450),
                     text_input="确定",font=get_hanzijianti_font(30),base_color="Black",hovering_color="White")
        next.changeColor(OPTIONS_MOUSE_POS)
        next.update(screen)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if next.checkForInput(OPTIONS_MOUSE_POS):
                    checkdisk()
                    
        #return
                    
        pygame.display.update()
        if get:
            return
def choosedisk():
    global running,bg_install   
    get=False
    while running:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        #screen.fill("cyan")

        screen.fill("black")
        screen.blit(bg_install,(0,0))
        ins_image=pygame.image.load("./running logo/setup-icon.png")
        insbt=Button(image=ins_image,pos=(30,30),
                     text_input=" ",font=get_font(1),base_color="white",hovering_color="white")
        insbt.changeColor(OPTIONS_MOUSE_POS)
        insbt.update(screen)
        OPTIONS_TEXT = get_hanzijianti_font(25).render("请选择硬盘：", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(150, 30))

        system_choose=Button(image=pygame.image.load("./running logo/system choose white.png"),pos=(500,281),text_input="",font=get_font(0),base_color="black",hovering_color="black")
        system_choose.changeColor(OPTIONS_MOUSE_POS)
        system_choose.update(screen)
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)
        disk=Button(image=pygame.image.load("./running logo/disk.png"),pos=(190,200),text_input="",font=get_font(0),base_color="black",hovering_color="black")
        disk.changeColor(OPTIONS_MOUSE_POS)
        disk.update(screen)
        g1=Button(image=None,pos=(300,200),
                  text_input="                                         C:/系统                   共100TB，72.5TB可用）",font=get_hanzijianti_font(20),base_color="Black",hovering_color="Black")
        g1.changeColor(OPTIONS_MOUSE_POS)
        g1.update(screen)
        copyright=Button(image=None,pos=(160,510),
                  text_input="© Github-Huangshaoqi 2023",font=get_hanzijianti_font(20),base_color="Black",hovering_color="black")
        copyright.changeColor(OPTIONS_MOUSE_POS)
        copyright.update(screen)
        copyright2=Button(image=None,pos=(120,535),
                  text_input="© happyleibniz 2023",font=get_hanzijianti_font(20),base_color="Black",hovering_color="black")
        copyright2.changeColor(OPTIONS_MOUSE_POS)
        copyright2.update(screen)        
        next=Button(image=pygame.image.load("./running logo/next_button.png"),pos=(800,450),
                     text_input="确定",font=get_hanzijianti_font(30),base_color="Black",hovering_color="White")
        next.changeColor(OPTIONS_MOUSE_POS)
        next.update(screen)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if next.checkForInput(OPTIONS_MOUSE_POS):
                    install()
                    
        #return
                    
        pygame.display.update()
        if get:
            return
def select_ver():
    global running,bg_install   
    get=False
    while running:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        #screen.fill("cyan")

        screen.fill("black")
        screen.blit(bg_install,(0,0))
        ins_image=pygame.image.load("./running logo/setup-icon.png")
        insbt=Button(image=ins_image,pos=(30,30),
                     text_input=" ",font=get_font(1),base_color="white",hovering_color="white")
        insbt.changeColor(OPTIONS_MOUSE_POS)
        insbt.update(screen)
        OPTIONS_TEXT = get_hanzijianti_font(25).render("请选择版本：", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(140, 30))

        system_choose=Button(image=pygame.image.load("./running logo/system choose white.png"),pos=(500,281),text_input="",font=get_font(0),base_color="black",hovering_color="black")
        system_choose.changeColor(OPTIONS_MOUSE_POS)
        system_choose.update(screen)
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)
        g1=Button(image=None,pos=(300,200),
                  text_input="                 PythonOS 测试版（build-1.5.2）",font=get_hanzijianti_font(20),base_color="Black",hovering_color="Black")
        g1.changeColor(OPTIONS_MOUSE_POS)
        g1.update(screen)
        copyright=Button(image=None,pos=(160,510),
                  text_input="© Github-Huangshaoqi 2023",font=get_hanzijianti_font(20),base_color="Black",hovering_color="black")
        copyright.changeColor(OPTIONS_MOUSE_POS)
        copyright.update(screen)
        copyright2=Button(image=None,pos=(120,535),
                  text_input="© happyleibniz 2023",font=get_hanzijianti_font(20),base_color="Black",hovering_color="black")
        copyright2.changeColor(OPTIONS_MOUSE_POS)
        copyright2.update(screen)        
        next=Button(image=pygame.image.load("./running logo/next_button.png"),pos=(800,450),
                     text_input="确定",font=get_hanzijianti_font(30),base_color="Black",hovering_color="White")
        next.changeColor(OPTIONS_MOUSE_POS)
        next.update(screen)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if next.checkForInput(OPTIONS_MOUSE_POS):
                    choosedisk()
                    
        #return
                    
        pygame.display.update()
        if get:
            return
def draw_progress_bar(value):
    global max_value
    progress_color = (0, 0, 255) # blue
    progress_width = int(value / max_value * 400)
    pygame.draw.rect(screen, progress_color, [10, 10, progress_width, 18], 0)
def running_backup_files():
    global running,bg_install,max_value,value
    get=False
    #progress_color = (0, 0, 255) # blue
    max_value = 100
    value = 0  
    while running:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        #screen.fill("cyan")

        screen.fill("black")
        screen.blit(bg_install,(0,0))
        OPTIONS_TEXT = get_hanzijianti_font(25).render("安装程序正在加载文件，请稍后...", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(500, 30))
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)
        ji=[
            pygame.image.load("./running logo/bar1.png"),
            pygame.image.load("./running logo/bar2.png"),
            pygame.image.load("./running logo/bar3.png"),
            pygame.image.load("./running logo/bar4.png"),
            pygame.image.load("./running logo/bar5.png"),
            ]
        draw_progress_bar(value)
        if value!=34.900000000000226:
            value += 0.1
        else:
            select_ver()
        

        copyright=Button(image=None,pos=(160,510),
                  text_input="© Github-Huangshaoqi 2023",font=get_hanzijianti_font(20),base_color="Black",hovering_color="black")
        copyright.changeColor(OPTIONS_MOUSE_POS)
        copyright.update(screen)
        copyright2=Button(image=None,pos=(120,535),
                  text_input="© happyleibniz 2023",font=get_hanzijianti_font(20),base_color="Black",hovering_color="black")
        copyright2.changeColor(OPTIONS_MOUSE_POS)
        copyright2.update(screen)



        #OPTIONS_BACK = Button(image=None, pos=(350, 480), 
        #                    text_input="BACK", font=get_font(20), base_color="Black", hovering_color="Green")

        #OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        #OPTIONS_BACK.update(screen)


        #return
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    value += 10 # increase the progress by 10% when space is pressed
                    if value > max_value:
                        value = max_value # cap the progress at 100%
        pygame.display.update()
        if get:
            return

def setup1():
    global running,bg_install
    get=False
    while running:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        #screen.fill("cyan")

        screen.fill("deepskyblue")
        screen.blit(bg_install,(0,0))
        system_choose=Button(image=pygame.image.load("./running logo/system choose white.png"),pos=(500,281),text_input="",font=get_font(0),base_color="black",hovering_color="black")
        system_choose.changeColor(OPTIONS_MOUSE_POS)
        system_choose.update(screen)
        #OPTIONS_TEXT = get_calibri_font(24).render("welcome to PythonOS 23H2 2402 build-1.5.2", True, "Black")
        #OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(310, 30))
        #screen.blit(OPTIONS_TEXT, OPTIONS_RECT)
        asktext1=get_hanzijianti_font(30).render('''欢迎来到PythonOS安装程序''',True,"Black")
        asktext1_rect=asktext1.get_rect(center=(500,50))
        #asktext2=get_hanzijianti_font(30).render('''请按照自己的习惯选择。完成后请点击“下一步”。''',True,"Black")
        #asktext2_rect=asktext1.get_rect(center=(540,100))
        screen.blit(asktext1,asktext1_rect)
        #screen.blit(asktext2,asktext2_rect)
        g1=Button(image=None,pos=(290,200), 
                  text_input="                 安装语言 : 中文简体 + English (USA)",font=get_hanzijianti_font(20),base_color="Black",hovering_color="gray")
        g1.changeColor(OPTIONS_MOUSE_POS)
        g1.update(screen)
        #国家与地区：
        g2=Button(image=None,pos=(230,230),
                  text_input="                 时间 & 地区 : 中国大陆",font=get_hanzijianti_font(20),base_color="Black",hovering_color="gray")
        g2.changeColor(OPTIONS_MOUSE_POS)
        g2.update(screen)
        #键盘格式：
        g3=Button(image=None,pos=(300,260),
                  text_input="                 键盘输入语言 : 中文-微软拼音/微软五笔",font=get_hanzijianti_font(20),base_color="Black",hovering_color="gray")
        g3.changeColor(OPTIONS_MOUSE_POS)
        g3.update(screen)
        copyright=Button(image=None,pos=(160,510),
                  text_input="© Github-Huangshaoqi 2023",font=get_hanzijianti_font(20),base_color="Black",hovering_color="black")
        copyright.changeColor(OPTIONS_MOUSE_POS)
        copyright.update(screen)
        copyright2=Button(image=None,pos=(120,535),
                  text_input="© happyleibniz 2023",font=get_hanzijianti_font(20),base_color="Black",hovering_color="black")
        copyright2.changeColor(OPTIONS_MOUSE_POS)
        copyright2.update(screen)
        login=Button(image=pygame.image.load("./running logo/next_button.png"),pos=(800,450),
                     text_input="确定",font=get_hanzijianti_font(30),base_color="Black",hovering_color="White")
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
                    print("byebye")
                    get=True
                    running_backup_files()
                    running=False
                    sys.exit()
                    
        #return
                    
        pygame.display.update()
        if get:
            return

def start():
    global running, bg_install
    get = False
    startuplist=[]
    
    for i in range(1,90):
        startuplist.append(pygame.image.load(f"./images/startup/startup_{i}.png"))
        print(startuplist)
    crraima=0

    screen.fill((0, 0, 0))
    #windows logo
    windows_leftup=pygame.image.load("./running logo/win1.png")
    windows_rightup=pygame.image.load("./running logo/win2.png")
    windows_leftdown=pygame.image.load("./running logo/win3.png")
    windows_rightdown=pygame.image.load("./running logo/win4.png")
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
    setup1()
    """
    for i in range(3000):
        screen.blit(windows_leftup,(305,15))
        screen.blit(windows_rightup,(440,15))
        screen.blit(windows_leftdown,(314,154))
        screen.blit(windows_rightdown,(449,153))
        screen.blit(startuplist[crraima], (370, 400))
        g1=Button(image=None,pos=(420,350),
        text_input="getting ready...",font=get_font(20),base_color="Orange",hovering_color="Orange")
        g1.changeColor(OPTIONS_MOUSE_POS)
        g1.update(screen)
        screen.blit(startuplist[crraima], (370, 400))
        
        pygame.display.flip()
        #clock.tick(25)
        pygame.display.update()
    screen.fill((0, 0, 0))
    g1.text_input=""
    for i in range(3000):
        screen.blit(windows_leftup,(305,15))
        screen.blit(windows_rightup,(440,15))
        screen.blit(windows_leftdown,(314,154))
        screen.blit(windows_rightdown,(449,153))
        screen.blit(startuplist[crraima], (370, 400))
        g1=Button(image=None,pos=(420,350),
        text_input="Configuring your device...",font=get_font(20),base_color="Orange",hovering_color="Orange")
        g1.changeColor(OPTIONS_MOUSE_POS)
        g1.update(screen)
        screen.blit(startuplist[crraima], (370, 400))
        
        pygame.display.flip()
        #clock.tick(25)
        pygame.display.update()
    screen.fill((0,0,0))
    g1.text_input=""
    for i in range(600):
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        screen.blit(windows_leftup,(305,15))
        screen.blit(windows_rightup,(440,15))
        screen.blit(windows_leftdown,(314,154))
        screen.blit(windows_rightdown,(449,153))
        screen.blit(startuplist[crraima], (370, 400))
        pygame.display.flip()
        clock.tick(25)
        crraima = (crraima + 1) % len(startuplist)
    screen.fill((0,0,0))
    for i in range(400):
        screen.blit(startuplist[crraima], (370, 400))
        pygame.display.flip()
        clock.tick(25)
        crraima = (crraima + 1) % len(startuplist)
    """
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

        if gg>=1000:
            start()
            sys.exit()
        gg+=1
        
    return
start_computer()