import pygame


class display:
    def __init__(self, x, y, id):
        #mise en place de la fonte de text
        self.textfont = pygame.font.SysFont("monospace", 35)
        self.x = x
        self.y = y
        self.id = id

    #affiche les montant de l'argent
    def draw_display(self, screen, money, money_ps):
        if self.id == 0:
            text_tbd = self.textfont.render("money: " + str(money), True, (0, 0, 0))
        elif self.id == 1:
            text_tbd = self.textfont.render("money per second:" + str(money_ps), True, (0, 0, 0))
        screen.blit(text_tbd, (self.x, self.y))
