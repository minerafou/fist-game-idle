import pygame


class money_display:
    def __init__(self):
        self.money = 0
        self.textfont = pygame.font.SysFont("monospace", 50)

    def earn_money(self, money_amount):
        self.money += money_amount

    def draw_money_display(self, screen):
        text_tbd = self.textfont.render("money: " + str(self.money), True, (0, 0, 0))
        screen.blit(text_tbd, (10, 10))
