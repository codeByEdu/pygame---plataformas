import pygame
import pygame_menu

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
        self.kills= 0
    def setup_level(self,layout):
        self.plataformas = pygame.sprite.Group()
        self.personagem = pygame.sprite.GroupSingle()
        self.zumbi = pygame.sprite.Group()
        self.layout = layout
        for row_index, row in enumerate(layout):
            for col_index,cell in enumerate(row):
                x = col_index * tam_plataforma
                y = row_index * tam_plataforma
                if cell == 'X':
                    plataforma = Plataforma((x,y),tam_plataforma, 'white')
                    self.plataformas.add(plataforma)
                elif cell=='P':
                    personagem = Personagem((x,y))
                    self.personagem.add(personagem)
                elif cell=='Z':
                    zumbi = Zumbi((x,y))
                    self.zumbi.add(zumbi)
                elif cell=='N':
                    plataforma = Plataforma((x,y),tam_plataforma, 'black')
                    self.plataformas.add(plataforma)
                elif cell=='M':
                    plataforma = Plataforma((x,y),tam_plataforma, 'red')
                    self.plataformas.add(plataforma)

    def restart(self, tela):
        if self.personagem.sprite.estado == 'morto':
            
            menu = pygame_menu.Menu("Você Morreu!", 300, 300, theme=pygame_menu.themes.THEME_BLUE )
            image_path = "Sprites/sad.png"
            menu.add.image(image_path, angle=10, scale=(0.15, 0.15))
           
            menu.add.button("Sair", pygame_menu.events.EXIT)
            menu.mainloop(tela)    
            

            
    def run(self):
        #level plataformas
        self.plataformas.update(self.world_shift, self.personagem.sprite)
        self.plataformas.draw(self.display_surface)

        #player
        personagem = self.personagem
        personagem.update()
        personagem.draw(self.display_surface)
        self.scroll_x()
        self.colisoes_horizontais()
        self.colisoes_verticais()
        self.attackEnemies()
        self.restart(self.display_surface)
        white = (255, 255, 255)
        green = (0, 255, 0)
        black = (0, 0, 0)
        font = pygame.font.Font('arial.ttf', 32)
        text = font.render(str("Vida"), True, green, black)
        text1 = font.render(str(int(self.personagem.sprite.life)), True, green, black)
        text2 = font.render(str("Pontos"), True, green, black)
        text3 = font.render(str(int(self.kills)), True, green, black)
        textRect = text.get_rect()
        textRect1 = text.get_rect()
        textRect2 = text.get_rect()
        textRect3 = text.get_rect()
        textRect.center = (1200 // 2, 100)
        textRect1.center = (1200 // 2, 150)
        textRect2.center = (1200 // 2, 200)
        textRect3.center = (1200 // 2, 250)
        self.display_surface.blit(text, textRect)
        self.display_surface.blit(text1, textRect1)
        self.display_surface.blit(text2, textRect2)
        self.display_surface.blit(text3, textRect3)

      

        if(personagem.sprite.atacando == True):
            print("ATACOU")
        # self.personagemAtaca()

        #zumbi
        self.zumbi.update(self.world_shift, self.personagem.sprite)
        self.zumbi.draw(self.display_surface)

    def personagemAtaca(self):
        fantasmas = self.zumbi
        print(fantasmas.__len__())

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

        if personagem.on_ground and personagem.direcao.y < 0 or personagem.direcao.y >1:
            personagem.on_ground = False
        if personagem.on_ceiling and personagem.direcao.y > 0:
            personagem.on_ceiling = False


    def attackEnemies(self):
        personagem = self.personagem.sprite
        hits = False
        if  personagem.atacando:
            hits = pygame.sprite.groupcollide(self.personagem,self.zumbi,False, True)
    
        if hits:
            self.kills+=1