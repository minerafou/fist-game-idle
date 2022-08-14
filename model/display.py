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
            money_tbd = self.adapt_money(money)
            text_tbd = self.textfont.render("money: " + str(money_tbd), True, (0, 0, 0))
        elif self.id == 1:
            money_tbd = self.adapt_money(money_ps)
            text_tbd = self.textfont.render("money per second:" + str(money_tbd), True, (0, 0, 0))
        screen.blit(text_tbd, (self.x, self.y))

    #ajoute K, M, B, AA, AB, AC etc...
    def adapt_money(self, money_before):
        if money_before >= 1000000000:
            money_divide = round(money_before / 1000000000, 2)
            money_after = (str(money_divide) + " B")
        elif money_before >= 1000000:
            money_divide = round(money_before / 1000000, 2)
            money_after = (str(money_divide) + " M")
        elif money_before >= 1000:
            money_divide = round(money_before / 1000, 2)
            money_after = (str(money_divide) + " K")
        else:
            return money_before
        return money_after
