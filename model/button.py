import pygame


class button:
    def __init__(self, x, y, width, height, color, screen):
        self.rect = (x, y, width, height)
        self.color = color
        self.screen = screen

    def draw_button(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def button_pressed(self):
        pass
