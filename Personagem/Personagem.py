import pygame
from .Bala import Bala
largura = 890
altura = 750
class Personagem(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Sprites/personagem.png')
        self.image = pygame.transform.scale(self.image, (60, 70))
        self.rect = self.image.get_rect()
        self.rect.centerx = largura/4
        self.rect.centery = altura/4
        self.life = 500
        self.velocidade = 25
       

    def colocar(self, superficie):
        superficie.blit(self.image, self.rect)

    def update(self):
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        self.rect.x += self.speedx
        if self.rect.right >  largura:
            self.rect.right = largura
        if self.rect.left < 0:
            self.rect.left = 0
        if keystate[pygame.K_UP]:
            self.speedy = -5
        self.rect.y += self.speedy
        if keystate[pygame.K_DOWN]:
            self.speedy = 8
        self.rect.y += self.speedy
        if self.rect.bottom >  altura:
            self.rect.bottom = altura
        if self.rect.top < 0:
            self.rect.top = 0
    def shoot(self, all_sprites,tiros):

        tiro = Bala(self.rect.centerx, self.rect.centery)
        all_sprites.add(tiro)
        tiros.add(tiro)    


        
