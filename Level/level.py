import pygame

from Personagem.Personagem import Personagem
from Personagem.Zumbi import Zumbi

from .Plataforma import Plataforma
from .settings import tam_plataforma, width


class level:
    def __init__(self,level_data,surface):
        # level setup
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0
        self.x_atual = 0

    def setup_level(self,layout):
        self.plataformas = pygame.sprite.Group()
        self.personagem = pygame.sprite.GroupSingle()
        self.zumbi = pygame.sprite.Group()
        for row_index, row in enumerate(layout):
            for col_index,cell in enumerate(row):
                if cell == 'X':
                    x = col_index * tam_plataforma
                    y = row_index * tam_plataforma
                    plataforma = Plataforma((x,y),tam_plataforma, 'white')
                    self.plataformas.add(plataforma)
                elif cell=='P':
                    x = col_index * tam_plataforma
                    y = row_index * tam_plataforma
                    personagem = Personagem((x,y))
                    self.personagem.add(personagem)
                elif cell=='Z':
                    x = col_index * tam_plataforma
                    y = row_index * tam_plataforma
                    zumbi = Zumbi((x,y))
                    self.zumbi.add(zumbi)
                elif cell=='N':
                    x = col_index * tam_plataforma
                    y = row_index * tam_plataforma
                    plataforma = Plataforma((x,y),tam_plataforma, 'black')
                    self.plataformas.add(plataforma)
                elif cell=='M':
                    x = col_index * tam_plataforma
                    y = row_index * tam_plataforma
                    plataforma = Plataforma((x,y),tam_plataforma, 'black')
                    self.plataformas.add(plataforma)


    def run(self):
        #level plataformas
        self.plataformas.update(self.world_shift)
        self.plataformas.draw(self.display_surface)
        #player
        self.personagem.update()
        self.personagem.draw(self.display_surface)
        self.scroll_x()
        self.colisoes_horizontais()
        self.colisoes_verticais()
        #zumbi
        self.zumbi.update(self.world_shift, self.personagem.sprite)
        self.zumbi.draw(self.display_surface)
        
        


    def scroll_x(self):
        personagem = self.personagem.sprite
        personagem_x = personagem.rect.centerx
        direction_x = personagem.direcao.x
        if personagem_x < width/4 and direction_x < 0:
            self.world_shift = 8
            personagem.velocidade = 0
        elif personagem_x >width- (width/4) and direction_x> 0 :
            self.world_shift = -8
            personagem.velocidade = 0
        else: 
            self.world_shift = 0
            personagem.velocidade = 8
    def colisoes_horizontais(self):
        personagem = self.personagem.sprite
        personagem.rect.x += personagem.direcao.x *personagem.velocidade
        for sprite in self.plataformas.sprites():
            if sprite.rect.colliderect(personagem.rect):
                if personagem.direcao.x< 0:
                    personagem.rect.left = sprite.rect.right
                    personagem.on_left = True
                    self.x_atual = personagem.rect.left
                elif personagem.direcao.x>0:
                    personagem.rect.right = sprite.rect.left
                    personagem.on_right = True
                    self.x_atual = personagem.rect.right
        if personagem.on_left and (personagem.rect.left < self.x_atual or personagem.direcao.x >= 0):
            personagem.on_left = False
        if personagem.on_right and (personagem.rect.right > self.x_atual or personagem.direcao.x <= 0):
            personagem.on_right = False

    def colisoes_verticais(self):
        personagem = self.personagem.sprite
        zumbi = self.zumbi.sprites()
        personagem.direcao.y += 1
        personagem.rect.y += personagem.direcao.y


        for sprite in self.plataformas.sprites():
            if sprite.rect.colliderect(personagem.rect):
                if personagem.direcao.y > 0:
                    
                    personagem.rect.bottom = sprite.rect.top
                    personagem.direcao.y = 0
                    personagem.on_ground = True
                    
                elif personagem.direcao.y < 0:
                    personagem.rect.top = sprite.rect.bottom
                    personagem.direcao.y = 0                    
                    personagem.on_ceiling = True

                # if zumbi.direcao.y > 0:
                    
                #     zumbi.rect.bottom = sprite.rect.top
                #     zumbi.direcao.y = 0
                #     zumbi.on_ground = True
        if personagem.on_ground and personagem.direcao.y < 0 or personagem.direcao.y >1:
            personagem.on_ground = False
        if personagem.on_ceiling and personagem.direcao.y > 0:
            personagem.on_ceiling = False