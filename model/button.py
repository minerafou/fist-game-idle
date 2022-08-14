from cgitb import text
import pygame
from model.additional_fonc import *


class button:
    #initialize la class bouton
    def __init__(self, x, y, width, height, color, color_over, color_not_buy, screen, text, cost, earn, earn_ps, earn_pc, coef_cost,
    unlock_cap, special_id):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.color_over = color_over
        self.color_not_buy = color_not_buy
        self.screen = screen
        self.text = text
        self.textfont_15px = pygame.font.SysFont("monospace", 15)
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
        self.special_id = special_id
        self.locked = True
        self.cap_bonus = [10, 25, 50, 75, 100, 150, 200, 250, 300, 400, 500, 600, 700, 800, 900, 1000, 1250, 1500, 1750, 2000, 1000000000]
        self.mult_bonus = [2, 2 , 2,  2,  5,   3,   3,   5,   5,   5,   5,   8,   8,   8,   8,   15,   15,   15,   25,   100,  0]
        self.level = 0

    def draw_button(self, money):
        #affiche le bouton

        text = self.textfont_15px.render(self.text , True, (0, 0, 0))
        text_rect = text.get_rect(center=(self.x + (self.width / 2), self.y + (self.height / 2)))

        #check la souris et la money pour la couleur du bouton
        mouse_pos = pygame.mouse.get_pos()
        if self.text == "Locked":
            pygame.draw.rect(self.screen, self.color_not_buy, self.rect)
        elif money < self.cost:
            pygame.draw.rect(self.screen, self.color_not_buy, self.rect)
        elif self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(self.screen, self.color_over, self.rect)
        else:
            pygame.draw.rect(self.screen, self.color, self.rect)
        self.screen.blit(text, text_rect)
        
        if self.special_id == "none":
            self.draw_bar()

    def button_pressed(self):
        #return true si la souris et sur le bouton
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            return True
        else:
            return False

    def set_earn_pc(self, earn_pc):
        #add des money par click au action du bouton
        self.earn = earn_pc

    def add_price(self, coef_mult):
        #augmente le price en fonction d'un coef
        self.cost = int(round(self.cost * coef_mult, 1))

    def get_action(self):
        #return les action de bouton
        self.action = (self.cost, self.coef_cost, self.special_id)
        return self.action

    def set_text(self, index, lifetime, money_pc):
        #set le text au bouton pour que sa change
        if self.is_locked(lifetime):
            self.text = ("Locked")
        
        elif index == 0:
            self.text = ("+" + str(adapt_money(money_pc)))
        elif index == 1:
            self.text = ("Exit")
        
        elif self.earn_ps == 0:
            text_earn = self.earn_text(self.earn_pc)
            self.text = ("Cost:" + str(adapt_money(self.cost)) + " +" + str(text_earn) + " per click")
        elif self.earn_pc == 0:
            text_earn = self.earn_text(self.earn_ps)
            self.text = ("Cost:" + str(adapt_money(self.cost)) + " +" + str(text_earn) + " per second")

    def add_level(self, up_level):
        self.level += up_level
    
    def get_money_pc_boost(self):
        boost_mult_cap = 1
        for i in self.cap_bonus:
            if self.level >= i:
                boost_mult_cap *= self.mult_bonus[self.cap_bonus.index(i)]
        return self.earn_pc * self.level * boost_mult_cap
    
    def get_money_ps_boost(self):
        boost_mult_cap = 1
        for i in self.cap_bonus:
            if self.level >= i:
                boost_mult_cap *= self.mult_bonus[self.cap_bonus.index(i)]
        return self.earn_ps * self.level * boost_mult_cap
    
    def is_locked(self, lifetime):
        if lifetime < self.unlock_cap:
            return True
        else:
            return False

    def check_next_cap(self):
        for i in self.cap_bonus:
            if self.level < i:
                return i

    def draw_bar (self):
        next_cap = self.check_next_cap()
        color_background = (170, 170, 170)
        color_progress = (130, 130, 130)

        if next_cap == 10:
            before_cap = 0
        else:
            before_cap = self.cap_bonus[self.cap_bonus.index(next_cap) - 1]

        progress = (self.level - before_cap) / (next_cap - before_cap)

        background_rect = (self.x, self.y + self.height, self.width, 20)
        progress_rect = (self.x, self.y + self.height, progress * self.width, 20)

        pygame.draw.rect(self.screen, color_background, background_rect)
        pygame.draw.rect(self.screen, color_progress, progress_rect)

        text_tbd = self.textfont_15px.render("Lvl: " + str(self.level) , True, (0, 0, 0))

        self.screen.blit(text_tbd, (self.x + 5, self.y + self.height + 1))

        text = "x" + str(self.mult_bonus[self.cap_bonus.index(self.check_next_cap())])
        text_tbd = self.textfont_15px.render(text, True, (0, 0, 0))
        text_width = text_tbd.get_width()

        self.screen.blit(text_tbd, (self.x + self.width - text_width, self.y + self.height + 1))

    def earn_text(self, text):
        boost_mult_cap = 1
        for i in self.cap_bonus:
            if self.level >= i:
                boost_mult_cap *= self.mult_bonus[self.cap_bonus.index(i)]
        text *= boost_mult_cap
        return adapt_money(text)
