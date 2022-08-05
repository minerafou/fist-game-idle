import pygame


class money_display:
    def __init__(self):
        #mise en place de la fonte de text
        self.textfont = pygame.font.SysFont("monospace", 50)

    #affiche les montant de l'argent
    def draw_money_display(self, screen, money):
        text_tbd = self.textfont.render("money: " + str(money), True, (0, 0, 0))
        screen.blit(text_tbd, (10, 10))
