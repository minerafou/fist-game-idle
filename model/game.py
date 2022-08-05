import pygame
from model.money_display import money_display
from model.button import button

#creation de la class 'game'
class game:
    def __init__(self, screen):
        #creation de la liste de boutton
        self.buttons = []
        #recuparation de la variable screen
        self.screen = screen
        #mise en place de la clock
        self.clock = pygame.time.Clock()
        #mise en place des variable
        self.running = True
        self.money_display = money_display()
        self.money = 0
        self.money_ps = 0
        self.money_pc = 1
        self.buttons.append(button(20, 100, 60, 60, (150, 150, 150), (180, 180, 180), self.screen, "+1", 0, 1, 0, 0))
        self.buttons.append(button(20, 200, 320, 60, (150, 150, 150), (180, 180, 180), self.screen, "cost:10 pc+0.1", 10, 0, 0, 0.1))

    def check_event(self):
        #verifie les input du joueur
        for event in pygame.event.get():
            #input de la croix rouge (en haut a droite de la fenetre)
            if event.type == pygame.QUIT:
                self.running = False
            
            #input de la souris
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in self.buttons:
                    if i.button_pressed():
                        cost, money_to_earn, increase_money_ps, increase_money_pc = i.get_action()
                        print(money_to_earn)
                        if self.check_for_money(cost):
                            self.earn_money(money_to_earn)
                            self.buy_money(cost)
                            self.increase_money_ps(increase_money_ps)
                            self.increase_money_pc(increase_money_pc)
                        

    def update(self):
        #delete tous sur l'ecran
        self.screen.fill((220, 220, 220))

        #affiche les different trucs
        #affachage de l'argent
        self.money_display.draw_money_display(self.screen, self.money)
        #affichage des boutons
        for i in self.buttons:
            i.draw_button()

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
        if self.money >= money_to_check:
            return True
        else:
            return False

    def earn_money(self, money_to_earn):
        self.money += money_to_earn

    def buy_money(self, price):
        self.money -= price
    
    def increase_money_ps(self, increase):
        self.money_ps += increase
    
    def increase_money_pc(self, increase):
        self.buttons[0].add_earn_pc(increase)
        self.money_pc += increase
    