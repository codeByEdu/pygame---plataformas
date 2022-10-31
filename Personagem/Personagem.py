import pygame
from .Bala import Bala
largura = 800
altura = 432




class Personagem(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load('Sprites/personagem.png')
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect(topleft = pos)
        self.life = 500
        self.velocidade = 4
        #self.direcao = 'direita'
        self.direcao = pygame.math.Vector2(0,0)
        self.pulando = False
        self.gravidade = 0.9
        self.pulo = -20
        self.velocidade_pulo = self.pulo
        self.stop = largura*0.55

    def colocar(self, superficie):
        superficie.blit(self.image, self.rect)

    def comandos(self):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a] :
            self.direcao.x = -2
            # self.direcao = 'esquerda'
             
        elif keystate[pygame.K_d] :
            self.direcao.x = 2
            # self.direcao = 'direita'
        else:
            self.direcao.x = 0

        if keystate[pygame.K_w]:
            self.jump()   
        
        
        # if self.rect.right >  largura:
        #     self.rect.right = largura
        # if self.rect.left < 0:
        #     self.rect.left = 0
     
    def update(self):
        self.comandos()
        
        
        
    def jump(self):
        self.direcao.y = self.pulo
        

        
    def shoot(self, all_sprites,tiros):

        tiro = Bala(self.rect.centerx, self.rect.centery, self.direcao)
        all_sprites.add(tiro)
        tiros.add(tiro)    


        
