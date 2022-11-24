import sys

import pygame

from .Bala import Bala
from .suporte import pasta

largura = 800
altura = 432

class Personagem(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.import_assets()
        self.frame_index = 0
        self.velocidade_animacao = 0.15
        self.image = self.animacoes['parado'][self.frame_index]
        self.rect = self.image.get_rect(topleft = pos)
        self.life = 5
        self.velocidade = 1
        self.direita = True
        self.direcao = pygame.math.Vector2(0,0)
        self.estado = 'parado'
        self.gravidade = 0.9
        self.pulo = -22
        self.velocidade_pulo = self.pulo
        self.stop = largura*0.55
        self.on_ground = False
        self.on_ceiling = False
        self.on_left = False
        self.on_right = False   

    def colocar(self, superficie):
        superficie.blit(self.image, self.rect, (0, 100, 255))

    def comandos(self):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a] :
            self.direcao.x = -1
            self.direita = False
        elif keystate[pygame.K_d] :
            self.direcao.x = 1
            self.direita = True
        else:
            self.direcao.x = 0
        if keystate[pygame.K_w]:
           if  self.on_ground == True:
                self.jump()
        if keystate[pygame.K_SPACE]:
            self.shoot()

    def morreu(self):
        self.estado = 'morto'     

    def update(self):
        self.comandos()
        self.animar_personagem()
        self.estado_personagem()

        if(self.rect.y >= 800):
            self.morreu()
        if self.life < 0:
            self.morreu()
    def jump(self):
        self.direcao.y = self.pulo
        
    def shoot(self):
        self.estado = 'atacando'
        self.velocidade_animacao = 0.5

    def levaDano(self):
        self.life -= 0.01

        

    def import_assets(self):
        caminho = 'Sprites/Personagem/'
        self.animacoes = {'parado':[],'correndo':[],'pulando':[], 'caindo':[], 'atacando':[]}
        for animacao in self.animacoes.keys():
            caminho_completo = caminho + animacao
            self.animacoes[animacao] = pasta(caminho_completo)

    def animar_personagem(self):
        if self.estado != 'morto':
            animacao = self.animacoes[self.estado]
            self.frame_index += self.velocidade_animacao
            if self.frame_index >= len(animacao):
                self.frame_index = 0
            imagem = animacao[int(self.frame_index)]
            imagem_virada = pygame.transform.flip(imagem,True,False)
            if self.direita:
                self.image = imagem
            else:
                self.image = imagem_virada
            if self.on_ground and self.on_right:
                self.rect = self.image.get_rect(bottomright = self.rect.bottomright) 
            elif self.on_ground and self.on_left:
                self.rect = self.image.get_rect(bottomleft = self.rect.bottomleft) 
            elif self.on_ground:
                self.rect = self.image.get_rect(midbottom = self.rect.midbottom)
            if self.on_ceiling and self.on_right:
                self.rect = self.image.get_rect(topright = self.rect.topright) 
            elif self.on_ceiling and self.on_left:
                self.rect = self.image.get_rect(topleft = self.rect.topleft) 
            elif self.on_ceiling:
                self.rect = self.image.get_rect(midtop = self.rect.midtop)

    def estado_personagem(self):
        if self.direcao.y < 0:
            self.estado = 'pulando'
        elif self.direcao.y > 1:
            self.estado = 'caindo'
        else:
            if self.direcao.x != 0:
                self.estado = 'correndo'
            else:
                self.estado = 'parado' 