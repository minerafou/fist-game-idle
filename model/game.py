import pygame
from model.money_display import money_display
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
        self.money_display = money_display()
        self.money_click = 1
        self.button1 = button(60, 60, 60, 60, (0, 255, 0), self.screen)

    def check_event(self):
        #verifie les input du joueur
        for event in pygame.event.get():
            #input de la croix rouge (en haut a droite de la fenetre)
            if event.type == pygame.QUIT:
                self.running = False
            #input de la souris
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.money_display.earn_money(self.money_click)
                print("mouse")
        print("check event")

    def update(self):
        #delete tous sur l'ecran
        self.screen.fill((30, 30, 30))
        #affiche les different trucs
        self.money_display.draw_money_display(self.screen)
        self.button1.draw_button()
        print("update")

    def refresh(self):
        #refresh l'ecran
        pygame.display.flip()
        print("refresh")

    def run(self):
        #boucle global du jeu
        while self.running:
            self.check_event()
            self.update()
            self.refresh()
            self.clock.tick(60)
            print("boucle")