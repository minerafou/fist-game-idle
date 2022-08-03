import pygame
from model.money_display import money_display
from model.button import button


class game:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.running = True
        self.money_display = money_display()
        self.money_click = 1
        self.button1 = button(60, 10, 60, 10)

    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.money_display.earn_money(self.money_click)

    def update(self):
        self.screen.fill((255, 255, 255))
        self.money_display.draw_money_display(self.screen)
        self.button1.draw_button(self.screen)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.check_event()
            self.update()
            self.clock.tick(60)
