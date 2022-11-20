import random
import sys

import pygame

from Level.level import level
from Level.settings import *
from Personagem.Bala import Bala
from Personagem.Personagem import Personagem
from Personagem.Zumbi import Zumbi

clock = pygame.time.Clock()
largura = 1200
altura = 700 

pygame.init()
tela = pygame.display.set_mode((largura, altura))
level = level(piece_main,tela)
pygame.display.set_caption("Pupo's attack")
all_sprites = pygame.sprite.Group()

tiros = pygame.sprite.Group()
jogando = True
enemies = pygame.sprite.Group()
scroll = 0 
bg_images = []


while jogando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    hits = pygame.sprite.groupcollide(enemies, tiros, True, True)
    for hit in hits:
        m = Zumbi(random.randrange(0, largura), 350)
        all_sprites.add(m)
        enemies.add(m)
    tela.fill('black')
    level.run()
    
    pygame.display.update()
    clock.tick(60)
