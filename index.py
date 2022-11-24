import random
import sys

import pygame
import pygame_menu

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
level = level(piece_main, tela)
pygame.display.set_caption("Pupo's attack")
all_sprites = pygame.sprite.Group()

tiros = pygame.sprite.Group()
jogando = True
enemies = pygame.sprite.Group()
scroll = 0
bg_imagews = []

nome = ""


def menuInicial():
    menu = pygame_menu.Menu("Bem vindo", 600, 500, theme=pygame_menu.themes.THEME_BLUE)

    nome = menu.add.text_input("Nome :", default="Pupo")

    menu.add.button("Jogar", start_the_game)
    menu.add.button("Sair", pygame_menu.events.EXIT)

    menu.mainloop(tela)
          

def start_the_game():
    while jogando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        level.run()

        pygame.display.update()

        clock.tick(60)
        tela.fill("black")


menuInicial()
enemies = pygame.sprite.Group()  
scroll = 0 
bg_imagews = []

while jogando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    level.run()
    pygame.display.update()
    clock.tick(60)
    tela.fill('black')

nome = ""


def menuInicial():
    menu = pygame_menu.Menu("Bem vindo", 600, 500, theme=pygame_menu.themes.THEME_BLUE)

    nome = menu.add.text_input("Nome :", default="Pupo")

    menu.add.button("Jogar", start_the_game)
    menu.add.button("Sair", pygame_menu.events.EXIT)

    menu.mainloop(tela)


def start_the_game():
    while jogando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        level.run()

        pygame.display.update()

        clock.tick(60)
        tela.fill("black")


menuInicial()
