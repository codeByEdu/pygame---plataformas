import os

import pygame


class Plataforma(pygame.sprite.Sprite):

    def __init__(self, pos,size, color):
        super().__init__()
        self.image = pygame.Surface((size,size))
        self.image.fill(color)
        if(color =='white'):
            self.image = pygame.image.load('Sprites/Cenario/piso.png')
        if(color == 'black'):
            image = pygame.Surface([64,64], pygame.SRCALPHA, 32)
            image = image.convert_alpha()  
            self.image = image
        self.rect = self.image.get_rect(topleft = pos)
    
    def update(self,x_shift, player):
        self.rect.x += x_shift