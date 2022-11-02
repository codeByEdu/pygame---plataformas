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
        self.life = 500
        self.velocidade = 4
        #self.direcao = 'direita'
        self.direcao = pygame.math.Vector2(0,0)
        self.pulando = False
        self.gravidade = 0.9
        self.pulo = -15
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
            if self.direcao.y >= 0 and self.pulando == False:
                self.jump()
                   
        
        
        # if self.rect.right >  largura:
        #     self.rect.right = largura
        # if self.rect.left < 0:
        #     self.rect.left = 0
     
    def update(self):
        self.comandos()
        self.animar_personagem()
        
        
    def jump(self):
        if self.pulando == False:
            self.direcao.y = self.pulo
            self.pulando == True

        
    def shoot(self, all_sprites,tiros):

        tiro = Bala(self.rect.centerx, self.rect.centery, self.direcao)
        all_sprites.add(tiro)
        tiros.add(tiro)    


    def import_assets(self):
        caminho = 'Sprites/Personagem/'
        self.animacoes = {'parado':[],'correndo':[],'pulando':[], 'caindo':[]}

        for animacao in self.animacoes.keys():
            caminho_completo = caminho + animacao
            self.animacoes[animacao] = pasta(caminho_completo)

    def animar_personagem(self):
        animacao = self.animacoes['parado']


        #loop sobre o frame_index

        self.frame_index += self.velocidade_animacao
        if self.frame_index >= len(animacao):
            self.frame_index = 0

        self.image = animacao[int(self.frame_index)]

