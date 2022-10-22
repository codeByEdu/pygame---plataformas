import pygame
import math
class Bala(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 20))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedx = -10
        self.speedy = -10
    def update(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
    
        distance_x = mouse_x - self.rect.centerx
        distance_y = mouse_y - self.rect.bottom
    
        angle = math.atan2(distance_y, distance_x)
    
        speed_x = 20 * math.cos(angle)
        speed_y = 20 * math.sin(angle)
        self.rect.x += speed_x
        self.rect.y += speed_y
        # kill if it moves off the top of the screen
        if self.rect.bottom < 0:
            self.kill()