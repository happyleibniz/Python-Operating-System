import sys
def get(gg=False):
    while True:
        if gg==True:
            break

def start_get():
    print("starting pygame...")
    try:
        import pygame
    except ImportError as e:
        print(e)
        print("import error")
    except not ImportError:
        print("unknown error!") 
    #get()



#pgzrun.go()