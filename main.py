import pygame
from model.game import game

#initialize pygame
pygame.init()

#set la fenetre
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("test python")

#cree le jeu a partir le l'objet 'game'
game = game(screen)

#lance la boucle global
game.run()

#quite pygame
pygame.quit()
