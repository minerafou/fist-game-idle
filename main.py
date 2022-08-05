import pygame
from model.game import game

#initialize pygame
pygame.init()

#start un event toute les 1 sec
pygame.time.set_timer(pygame.USEREVENT, 10)

#set taille fenetre
screen_width = 1200

screen_height = 800

#set la fenetre
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("test python")

#cree le jeu a partir le l'objet 'game'
game1 = game(screen, screen_width, screen_height)

#lance la boucle global
game1.run()

#quite pygame
pygame.quit()
