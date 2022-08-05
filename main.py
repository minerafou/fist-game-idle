import pygame
from model.game import game

#initialize pygame
pygame.init()

#set la fenetre
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("test python")

#cree le jeu a partir le l'objet 'game'
game1 = game(screen)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 252))
    pygame.display.flip()

#lance la boucle global
game1.run()

print("quit")

#quite pygame
pygame.quit()
