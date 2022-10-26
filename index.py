import pygame
import sys
import random
from Personagem.Personagem import Personagem
from Personagem.Zumbi import Zumbi
from Personagem.Bala import Bala

clock = pygame.time.Clock()
largura = 800
altura = 432

pygame.init()
tela = pygame.display.set_mode((largura, altura))



#imagemFundo = pygame.image.load('Sprites/bg.jpg')
pygame.display.set_caption("RPG do SI")
all_sprites = pygame.sprite.Group()
jogador = Personagem()
all_sprites.add(jogador)
tiros = pygame.sprite.Group()
jogando = True
grupo_de_alvos = pygame.sprite.Group()

for i in range(5):
    zumbi = Zumbi(random.randrange(0, largura), 350)
    grupo_de_alvos.add(zumbi)
scroll = 0 
ground_image = pygame.image.load('Sprites/ground.png').convert_alpha()
ground_width = ground_image.get_width()
ground_height = ground_image.get_height()

bg_images = []
for i in range(1, 6):
  bg_image = pygame.image.load(f'Sprites/plx-{i}.png').convert_alpha()
  bg_images.append(bg_image)
bg_width = bg_images[0].get_width()

def draw_bg():
  for x in range(5):
    speed = 1
    for i in bg_images:
      tela.blit(i, ((x * bg_width) - scroll * speed, 0))
      speed += 0.2

def draw_ground():
  for x in range(15):
    tela.blit(ground_image, ((x * ground_width) - scroll * 2.5, altura - ground_height))

while jogando:
    draw_bg()
    draw_ground()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                
                jogador.shoot(all_sprites,tiros)
    key = pygame.key.get_pressed()
    if key[pygame.K_a] and scroll > 0:
        scroll -= 3
        all_sprites.update()
    if key[pygame.K_d] and scroll < 3000:
        scroll += 3
        all_sprites.update()

    all_sprites.update()
    
    tela.blit(ground_image, (0, 0))
    grupo_de_alvos.draw(tela)
    jogador.colocar(tela)
    pygame.display.update()
    all_sprites.draw(tela)
    pygame.display.flip()
    clock.tick(60)
