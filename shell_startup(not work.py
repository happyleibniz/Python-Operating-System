import threading
import terminal
terminal_start_get_1=threading.Thread(target=terminal.start_get())
import pygame
import pgzrun
import platform
import random
import psutil
vm_info="Pyvm1.0"
booter="Py legends"
os_name = platform.system()
os_version = platform.version()
cpu_info = platform.processor()
ram_info = platform.machine()
WIDTH=700
HEIGHT=500
pyos_pos=(350,10)
is_white=False
if is_white==False:
    bg="background_black"
    pythonos_black=Actor("pythonos_white")
    #pythonos_black.image.set_alpha()
    pythonos_black.pos=pyos_pos
pylegends_pos=(150,30)
pylegends=Actor("pylegends2")
pylegends.pos=pylegends_pos
processes = psutil.process_iter()
def draw():
    global booter
    screen.blit(bg,(0,0))
    start=True
    if start==True:
        if is_white==False:
            pythonos_black.draw()
            pylegends.draw()
        screen.draw.text("os:"+str(os_name),color="white",topleft=(10,60))
        screen.draw.text("os_ver:"+str(os_version),color="white",topleft=(10,75))
        screen.draw.text("cpu_info:"+str(cpu_info),color="white",topleft=(10,90))
        screen.draw.text("ram_info:"+str(ram_info),color="white",topleft=(10,105))
        screen.draw.text("vm version:"+str(vm_info),color="white",topleft=(10,120))
        screen.draw.text("booter:"+str(booter),color="white",topleft=(10,135))
        evthing_ready="no"
        #gut.visible=True
        gut=screen.draw.text("bios,settings,desktop,etc?--"+str(evthing_ready),color="white",topleft=(10,150))
        rewrite=0
        for i in range(10000):
            rewrite+=1
        evthing_ready="Yes"
        gut.visible=False
        screen.draw.text("bios,settings,desktop,etc?--"+str(evthing_ready),color="white",topleft=(10,150))
    else:
        pass
"""
    check_usage=True
    if check_usage:
        current_process = psutil.Process()
        cpu_usage = current_process.cpu_percent(interval=1)
        screen.draw.text("cpu:"+str(cpu_usage),color="white",topleft=(10,120))
    check_usage=False
"""
def update():
    #global cpu_percent,processes
    pass

pgzrun.go()