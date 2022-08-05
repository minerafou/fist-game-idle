import pygame
from model.display import display
from model.button import button

#creation de la class 'game'
class game:
    def __init__(self, screen):
        #recuparation de la variable screen
        self.screen = screen
        #mise en place de la clock
        self.clock = pygame.time.Clock()
        #mise en place des variable
        self.running = True
        self.money_display = display(20, 10, 0)
        self.money_ps_display = display(400, 10, 1)
        self.money = 0
        self.money_ps = 0
        self.money_pc = 1
        #creation de la liste de boutton
        self.buttons = []
        #skockage des button dans une liste

        #button du clic
        self.buttons.append(button(20, 100, 80, 80, (180, 180, 180), (150, 150, 150), (100, 100, 100), self.screen, "+10", 0, 10, 0, 0, 0, 0))

        #upgrade click 1
        self.buttons.append(button(20, 200, 320, 80, (180, 180, 180), (150, 150, 150), (100, 100, 100), self.screen, "cost:100 pc+1", 150, 0, 0, 1, 1.03, 150))
        
        #upgrade click 2
        self.buttons.append(button(20, 300, 320, 80, (180, 180, 180), (150, 150, 150), (100, 100, 100), self.screen, "cost:100 pc+1", 1000, 0, 0, 12, 1.03, 1500))
        
        #upgrade income 1
        self.buttons.append(button(400, 200, 320, 80, (180, 180, 180), (150, 150, 150), (100, 100, 100), self.screen, "cost:100 pc+1", 100, 0, 1, 0, 1.03, 500))

        #upgrade income 1
        self.buttons.append(button(400, 300, 320, 80, (180, 180, 180), (150, 150, 150), (100, 100, 100), self.screen, "cost:100 pc+1", 2000, 0, 25, 0, 1.03, 4000))
        
        self.lifetime = 0
    def check_event(self):
        #verifie les input du joueur
        for event in pygame.event.get():
            #input de la croix rouge (en haut a droite de la fenetre)
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.USEREVENT:
                self.add_money_ps()
            
            #input de la souris
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                #check des buttons
                for i in self.buttons:
                    if i.button_pressed():

                        #recupation des action du bouton
                        cost, money_to_earn, increase_money_ps, increase_money_pc, coef_cost = i.get_action()

                        #check de l'argent
                        if self.check_for_money(cost):

                            #fait les action du bouton
                            self.earn_money(money_to_earn)
                            self.buy_money(cost)
                            self.increase_money_ps(increase_money_ps)
                            self.increase_money_pc(increase_money_pc)
                            i.add_price(coef_cost)

                        

    def update(self):
        #delete tous sur l'ecran
        self.screen.fill((220, 220, 220))

        #affachage des l'argents
        self.money_display.draw_display(self.screen, self.money, self.money_ps)
        self.money_ps_display.draw_display(self.screen, self.money, self.money_ps)
        
        #affichage des boutons
        for i in self.buttons:
            #set text test aussi si le bouton est unlock
            i.set_text(self.buttons.index(i), self.lifetime)
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
            self.clock.tick(60)

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
    
    def increase_money_ps(self, increase):
        #add de la money par seconde
        self.money_ps += increase
    
    def increase_money_pc(self, increase):
        #add de la money par click
        self.buttons[0].add_earn_pc(increase)
        self.money_pc += increase

    def add_money_ps(self):
        self.money += self.money_ps
        self.lifetime += self.money_ps
