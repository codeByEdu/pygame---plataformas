import os

import pygame


class Plataforma(pygame.sprite.Sprite):

    def __init__(self, pos,size, color):
        super().__init__()
        self.image = pygame.Surface((size,size))
        self.image.fill(color)
        if(color != 'black'):
            self.image = pygame.image.load('Sprites\Cenario\piso.png')
        self.rect = self.image.get_rect(topleft = pos)
    
    def update(self,x_shift):
        self.rect.x += x_shift