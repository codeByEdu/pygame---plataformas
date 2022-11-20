import math

import pygame

from .suporte import pasta


class Zumbi(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.import_assets()
        self.frame_index = 0
        self.velocidade_animacao = 0.15
        self.image = self.animacoes['Parado'][self.frame_index]
        self.image = pygame.transform.scale(self.image ,(76,56))
        self.estado = 'Parado'
        self.direita = True
        self.rect = self.image.get_rect(topleft = pos)
        self.speed = 2
        self.rect = self.image.get_rect(topleft = pos)
        self.direcao = pygame.math.Vector2(1,1)
        self.on_ground = False
        self.on_ceiling = False
        self.on_left = False
        self.on_right = False

    def update(self,x_shift, player):
        self.rect.x += x_shift
        self.animar_personagem()
        self.estado_personagem()
        self.move_towards_player2(player)
    
    def caminhar(self):
        self.direcao.x = -1
        self.direita = False

    def move_towards_player2(self, player):
        dirvect = pygame.math.Vector2(player.rect.x - self.rect.x,
                                        player.rect.y - self.rect.y)
        dirvect.normalize()
        dirvect.scale_to_length(self.speed)
        self.rect.move_ip(dirvect)
        
    def import_assets(self):
        caminho = 'Sprites/Zumbi/'
        self.animacoes = {'Parado':[],'Andando':[],'Morto':[], 'Atacando':[]}

        for animacao in self.animacoes.keys():
            caminho_completo = caminho + animacao
            self.animacoes[animacao] = pasta(caminho_completo)

    def animar_personagem(self):
        animacao = self.animacoes[self.estado]
        self.frame_index += self.velocidade_animacao
        if self.frame_index >= len(animacao):
            self.frame_index = 0
        imagem = animacao[int(self.frame_index)]
        imagem_virada = pygame.transform.flip(imagem,True,False)
        if self.direita:
            self.image  = pygame.transform.scale(imagem ,(64,64))
        else:
            self.image = pygame.transform.scale(imagem_virada ,(64,64))
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
        if self.direcao.x != 0:
            self.estado = 'Andando'
        else:
            self.estado = 'Parado' 
       

