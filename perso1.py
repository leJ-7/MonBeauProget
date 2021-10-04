import pygame


class Perso():
    
    def __init__(self):
        
        self.image = pygame.image.load("guts1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.velocity = 5
        self.sante = 100
        self.armure = 100
        self.puissance = 15
        self.munition = 0


    def mouv_right(self):
        self.rect.x += self.velocity
    def mouv_left(self):
        self.rect.x -= self.velocity
    def mouv_up(self):
        self.rect.y -= self.velocity
    def mouv_down(self):
        self.rect.y += self.velocity
        