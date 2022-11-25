import pygame

class Attack(pygame.sprite.Sprite):
    def __init__(self, enemies, x,y ):
        super().__init__()
        self.image = pygame.Surface([32,64])
        self.image.fill((255,255,255))
        self.image.get_rect.x = x
        self.image.get_rect.y = y
        self.image.convert_alpha()  
        self.enemies = enemies
        

    def collide(self):
        hits = pygame.sprite.spritecollide(self,self.enemies, True)

    def update(self):

        self.collide()

    
    