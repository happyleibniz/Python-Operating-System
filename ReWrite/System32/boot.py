import hid
import pygame
from . import *


class Power_On_Self_Tester:
    def __init__(self):
        self.Display = None
        self.keyboard = None
        self.cpu_check_stats = None
        self.memory_check_stats = None
        # // 答辩论证

    def POST(self):
        self.cpu_check_stats = CpuCheck()
        self.cpu_check_stats = self.cpu_check_stats.cpu_info()
        self.cpu_check_stats = MemCheck()
        self.memory_check_stats = self.cpu_check_stats.check()
        self.bios_init()
        self.Peripheral_Detection()
        self.Power_Supply_Check()
        self.BIOS_UEFI_Configuration_Check()
        self.Display_Test()
        self.keyboard_input_check()

    def bios_init(self):
        pass

    def Peripheral_Detection(self):
        pass

    def BIOS_UEFI_Configuration_Check(self):
        pass

    def Power_Supply_Check(self):
        pass

    def Display_Test(self):
        try:
            pygame.init()
            screen = pygame.display.set_mode((400, 300))
            pygame.display.set_caption("Display Test - Pygame")
            screen.fill((255, 255, 255))
            pygame.draw.rect(screen, (255, 0, 0), (150, 100, 100, 100))
            pygame.quit()
            self.Display = True
        except Exception as e:
            print("Error: " + str(e))
            print("aborting Power On Self Test")
            self.Display = False
            exit(-1073741510)

    def keyboard_input_check(self):
        try:
            devices = hid.enumerate()
            for device in devices:
                if "keyboard" in device['product_string'].lower():
                    self.keyboard = True
                    return
            self.keyboard = False
        except Exception as e:
            print("Error:", e)
            print("aborting Power On Self Test")
            self.keyboard = False
            exit(-1073741510)

    def get_var(self):
        return [self.keyboard, self.Display]


class BIOS(Power_On_Self_Tester):
    def __init__(self, *args, **kwargs):
        super().__init__()

