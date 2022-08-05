import pygame
from model.money_display import money_display


class button:
    def __init__(self, x, y, width, height, color, color_pos, screen, text, cost, earn, earn_ps, earn_pc):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.color_pos = color_pos
        self.screen = screen
        self.text = text
        self.textfont = pygame.font.SysFont("monospace", 30)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.cost = cost
        self.earn = earn
        self.earn_ps = earn_ps
        self.earn_pc = earn_pc

    def draw_button(self):
        #affiche le bouton
        mouse_pos = pygame.mouse.get_pos()
        text = self.textfont.render(self.text , True, (0, 0, 0))
        text_rect = text.get_rect(center=(self.x + (self.width / 2), self.y + (self.height / 2)))
        
        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(self.screen, self.color, self.rect)
        else:
            pygame.draw.rect(self.screen, self.color_pos, self.rect)
        self.screen.blit(text, text_rect)

    def button_pressed(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            return True
        else:
            return False

    def add_earn_pc(self, increase):
        self.earn += increase

    def get_action(self):
        self.action = (self.cost, self.earn, self.earn_ps, self.earn_pc)
        return self.action