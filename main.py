import pygame
from model.game import game

pygame.init()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("_____")

game = game(screen)

game.run()

pygame.quit()
