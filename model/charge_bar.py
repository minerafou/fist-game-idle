import pygame

class ChargeBar:
    def __init__(self, x, y, width, height, speed, color_background, color_progress):
        self.x = x
        self.y = y
        self.width = width
        self.width_progress = width
        self.height = height
        self.speed = speed
        self.progress = 0
        self.rect_background = (self.x, self.y, self.width, self.height)
        self.rect_progress = self.rect_background
        self.color_background = color_background
        self.color_progress = color_progress
    
    def draw_bar(self, screen):
        self.width_progress = int(round(self.width * (self.progress / self.speed) / 100, 1))
        self.rect_progress = (self.x, self.y, self.width_progress, self.height)
        pygame.draw.rect(screen, self.color_background, self.rect_background)
        pygame.draw.rect(screen, self.color_progress, self.rect_progress)

    def update(self):
        self.progress += 1
        if self.progress == 100*self.speed:
            self.progress = 0
