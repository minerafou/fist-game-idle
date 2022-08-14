import pygame
from model.display import display
from model.button import button
from model.charge_bar import charge_bar

#creation de la class 'game'
class game:
    def __init__(self, screen, screen_width, screen_height):
        #recuparation de la variable screen et de variable de taille
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = screen

        #mise en place de la clock
        self.clock = pygame.time.Clock()

        #mise en place de la bar des seconde
        self.charge_bar = charge_bar(400, 50, 375, 10, 1, (170, 170, 170), (100, 100, 100))

        #mise en place des variable
        self.running = True
        self.money_display = display(20, 10, 0)
        self.money_ps_display = display(400, 10, 1)
        self.money = 0
        self.money_ps = 0
        self.money_pc = 10
        self.counter_sec = 1
        self.lifetime = 0

        #creation de la liste de boutton
        self.buttons = []

        #skockage des button dans une liste

        #button du clic
        self.buttons.append(button(20, 100, 80, 80, (180, 180, 180), (150, 150, 150), (100, 100, 100), 
        self.screen, "+10", 0, 10, 0, 0, 0, 0, "click"))

        #button exit
        self.buttons.append(button(self.screen_width-120, 0, 120, 80, (180, 180, 180), (150, 150, 150), (100, 100, 100),
        self.screen, "+10", 0, 0, 0, 0, 0, 0, "exit"))

        #upgrade click 1
        self.buttons.append(button(20, 200, 320, 60, (180, 180, 180), (150, 150, 150), (100, 100, 100), 
        self.screen, "cost:100 pc+1", 100, 0, 0, 1, 1.09, 100, "none"))
        
        #upgrade click 2
        self.buttons.append(button(20, 300, 320, 60, (180, 180, 180), (150, 150, 150), (100, 100, 100), 
        self.screen, "cost:100 pc+1", 1000, 0, 0, 12, 1.09, 5000, "none"))

        #upgrade click 3
        self.buttons.append(button(20, 400, 320, 60, (180, 180, 180), (150, 150, 150), (100, 100, 100), 
        self.screen, "cost:100 pc+1", 7500, 0, 0, 95, 1.09, 35000, "none"))

        #upgrade click 4
        self.buttons.append(button(20, 500, 320, 60, (180, 180, 180), (150, 150, 150), (100, 100, 100), 
        self.screen, "cost:100 pc+1", 35000, 0, 0, 150, 1.09, 100000, "none"))
        
        #upgrade income 1
        self.buttons.append(button(400, 200, 320, 60, (180, 180, 180), (150, 150, 150), (100, 100, 100), 
        self.screen, "cost:100 pc+1", 100, 0, 1, 0, 1.09, 500, "none"))

        #upgrade income 2
        self.buttons.append(button(400, 300, 320, 60, (180, 180, 180), (150, 150, 150), (100, 100, 100), 
        self.screen, "cost:100 pc+1", 2500, 0, 35, 0, 1.09, 10000, "none"))

        #upgrade income 3
        self.buttons.append(button(400, 400, 320, 60, (180, 180, 180), (150, 150, 150), (100, 100, 100), 
        self.screen, "cost:100 pc+1", 10000, 0, 140, 0, 1.09, 90000, "none"))

        #upgrade income 4
        self.buttons.append(button(400, 500, 320, 60, (180, 180, 180), (150, 150, 150), (100, 100, 100), 
        self.screen, "cost:100 pc+1", 50000, 0, 300, 0, 1.09, 250000, "none"))
        
    def check_event(self):
        #verifie les input du joueur
        for event in pygame.event.get():
            #input de la croix rouge (en haut a droite de la fenetre)
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.USEREVENT:
                self.every_milsec_action()
            
            #input de la souris
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                #check des buttons
                self.check_button()

    def update(self):
        #delete tous sur l'ecran
        self.screen.fill((220, 220, 220))

        #affachage des l'argents
        self.money_display.draw_display(self.screen, self.money, self.money_ps)
        self.money_ps_display.draw_display(self.screen, self.money, self.money_ps)
        
        #affiche la bar
        self.charge_bar.draw_bar(self.screen)
        #affichage des boutons
        for i in self.buttons:
            #set text test aussi si le bouton est unlock
            i.set_text(self.buttons.index(i), self.lifetime, self.money_pc)
            i.draw_button(self.money)

    def refresh(self):
        #refresh l'ecran
        pygame.display.flip()

    def run(self):
        #boucle global du jeu
        while self.running:
            self.check_event()
            self.update()
            self.refresh()

    def check_for_money(self, money_to_check):
        #check la quantite d'argent
        if self.money >= money_to_check:
            return True
        else:
            return False

    def earn_money(self, money_to_earn):
        #add de l'argent
        self.money += money_to_earn
        self.lifetime += money_to_earn

    def buy_money(self, price):
        #enleve de l'argent
        self.money -= price

    def add_money_ps(self):
        self.earn_money(self.money_ps)

    def every_milsec_action(self):
        #informa charge bar que 10ms ce sont ecouler
        self.charge_bar.update()

        #add la money toute les sec
        self.counter_sec += 1
        if self.counter_sec == 100:
            self.counter_sec = 0
            self.add_money_ps()

    def check_button(self):
        for i in self.buttons:
            if i.button_pressed() and not i.is_locked(self.lifetime):

                #recupation des action du bouton
                cost, coef_cost, special_id = i.get_action()

                #check click button
                if special_id == "click":
                    self.earn_money(self.money_pc)            
                
                #check exit button
                elif special_id == "exit":
                    self.running = False

                #check de l'argent
                elif self.check_for_money(cost):

                    #fait les action du bouton
                    i.add_level(1)
                    self.check_money_pc_ps()
                    self.buy_money(cost)
                    i.add_price(coef_cost)

    def check_money_pc_ps(self):
        self.money_ps = 0
        self.money_pc = 10
        for i in self.buttons:
            self.money_pc += i.get_money_pc_boost()
            self.money_ps += i.get_money_ps_boost()
