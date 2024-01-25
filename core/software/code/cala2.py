import pygame
import sys

class Calculator:
    def __init__(self):
        pygame.init()

        self.width, self.height = 450, 500
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("计算器")

        self.clock = pygame.time.Clock()

        self.result_text = ""
        self.font = pygame.font.Font(None, 36)

        self.create_buttons()

    def create_buttons(self):
        button_layout = [
            ('7', 50, 100), ('8', 150, 100), ('9', 250, 100), ('/', 350, 100),
            ('4', 50, 200), ('5', 150, 200), ('6', 250, 200), ('*', 350, 200),
            ('1', 50, 300), ('2', 150, 300), ('3', 250, 300), ('-', 350, 300),
            ('0', 50, 400), ('C', 150, 400), ('=', 250, 400), ('+', 350, 400),
        ]

        self.buttons = []
        for text, x, y in button_layout:
            button_rect = pygame.Rect(x, y, 80, 80)
            button = {'rect': button_rect, 'text': text}
            self.buttons.append(button)

    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.draw()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.check_button_click(event.pos)

    def check_button_click(self, pos):
        for button in self.buttons:
            if button['rect'].collidepoint(pos):
                self.on_button_click(button['text'])
                break

    def on_button_click(self, value):
        if value == 'C':
            self.result_text = ''
        elif value == '=':
            try:
                result = eval(self.result_text)
                self.result_text = str(result)
            except Exception as e:
                self.result_text = '错误'
        else:
            self.result_text += value

    def update(self):
        pass

    def draw(self):
        self.screen.fill((255, 255, 255))

        result_surface = self.font.render(self.result_text, True, (0, 0, 0))
        result_rect = result_surface.get_rect(center=(self.width // 2, 50))
        self.screen.blit(result_surface, result_rect)

        for button in self.buttons:
            pygame.draw.rect(self.screen, (0, 0, 0), button['rect'], 2)
            button_surface = self.font.render(button['text'], True, (0, 0, 0))
            button_rect = button_surface.get_rect(center=button['rect'].center)
            self.screen.blit(button_surface, button_rect)

        pygame.display.flip()
        self.clock.tick(30)

if __name__ == "__main__":
    calculator = Calculator()
    calculator.run()
