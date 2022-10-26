import pygame
from .Bala import Bala
largura = 800
altura = 432




class Personagem(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Sprites/personagem.png')
        self.image = pygame.transform.scale(self.image, (60, 70))
        self.rect = self.image.get_rect()
        self.rect.centerx = largura/3
        self.rect.centery = 350
        self.life = 500
        self.velocidade = 25
        self.direcao = 'direita'
        self.pulando = False
        self.gravidade = 1
        self.pulo = 20
        self.velocidade_pulo = self.pulo
        self.stop = largura*0.55

    def colocar(self, superficie):
        superficie.blit(self.image, self.rect)

    def update(self):
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a] :
            self.speedx = 3
            self.direcao = 'esquerda'
            self.rect.x -= self.speedx   
        if keystate[pygame.K_d] :
            self.speedx = 3
            self.direcao = 'direita'
            if self.rect.centerx < self.stop:    
                self.rect.x += self.speedx
        if self.rect.right >  largura:
            self.rect.right = largura
        if self.rect.left < 0:
            self.rect.left = 0
        if keystate[pygame.K_w]:
            self.pulando = True
            self.speedy = -5
        #self.rect.y += self.speedy
        #if keystate[pygame.K_DOWN]:
            #self.speedy = 8
        #self.rect.y += self.speedy
        if self.rect.bottom >  altura:
            self.rect.bottom = altura
        if self.rect.top < 0:
            self.rect.top = 0
        if self.pulando:
            self.rect.y -= self.velocidade_pulo
            self.velocidade_pulo -= self.gravidade
            if self.velocidade_pulo < - self.pulo:
                self.pulando = False
                self.velocidade_pulo = self.pulo
    def shoot(self, all_sprites,tiros):

        tiro = Bala(self.rect.centerx, self.rect.centery, self.direcao)
        all_sprites.add(tiro)
        tiros.add(tiro)    


        
