import pygame


class button:
    #initialize la class bouton
    def __init__(self, x, y, width, height, color, color_over, color_not_buy, screen, text, cost, earn, earn_ps, earn_pc, coef_cost, unlock_cap):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.color_over = color_over
        self.color_not_buy = color_not_buy
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
        self.coef_cost = coef_cost
        self.unlock_cap = unlock_cap
        self.locked = True

    def draw_button(self, money):
        #affiche le bouton

        text = self.textfont.render(self.text , True, (0, 0, 0))
        text_rect = text.get_rect(center=(self.x + (self.width / 2), self.y + (self.height / 2)))

        #check la souris et la money pour la couleur du bouton
        mouse_pos = pygame.mouse.get_pos()
        if self.text == "locked":
            pygame.draw.rect(self.screen, self.color_not_buy, self.rect)
        elif money < self.cost:
            pygame.draw.rect(self.screen, self.color_not_buy, self.rect)
        elif self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(self.screen, self.color_over, self.rect)
        else:
            pygame.draw.rect(self.screen, self.color, self.rect)
        self.screen.blit(text, text_rect)

    def button_pressed(self):
        #return true si la souris et sur le bouton
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            return True
        else:
            return False

    def add_earn_pc(self, increase):
        #add des money par click au action du bouton
        self.earn += increase

    def add_price(self, coef_mult):
        #augmente le price en fonction d'un coef
        self.cost = int(round(self.cost * coef_mult, 1))

    def get_action(self):
        #return les action de bouton
        self.action = (self.cost, self.earn, self.earn_ps, self.earn_pc, self.coef_cost)
        return self.action

    def set_text(self, index, lifetime):
        #set le text au bouton pour que sa change
        if lifetime < self.unlock_cap:
            self.text = ("locked")
        elif index == 0:
            self.text = ("+" + str(self.earn))
        elif index == 1:
            self.text = ("cost:" + str(self.cost) + " +" + str(self.earn_pc) + "pc")
        elif index == 2:
            self.text = ("cost:" + str(self.cost) + " +" + str(self.earn_pc) + "pc")
        elif index == 3:
            self.text = ("cost:" + str(self.cost) + " +" + str(self.earn_ps) + "ps")