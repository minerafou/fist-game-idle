import pygame

class charge_bar:
    def __init__(self, x, y, width, height, speed):
        self.x = x
        self.y = y
        self.widht = width
        self.height = height
        self.speed = speed
        self.progression = 0
    
    def draw_bar(screen):
        pass

    def update(self):
        self.progression += 1
        if self.progression == 100:
            self.progression = 0
