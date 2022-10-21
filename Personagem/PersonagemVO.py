import pygame
import sys
import random
clock = pygame.time.Clock()
largura = 890
altura = 750

class Inimigo(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load("../Sprites/zumbi.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]


class Personagem(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.personagem = pygame.image.load('../Sprites/personagem.png')
        self.personagem = pygame.transform.scale(self.personagem, (60, 70))
        self.rect = self.personagem.get_rect()
        self.rect.centerx = largura/4
        self.rect.centery = altura/4
        self.life = 500
        self.velocidade = 10

    def colocar(self, superficie):
        superficie.blit(self.personagem, self.rect)


def rpg():
    pygame.init()
    imagemFundo = pygame.image.load('../Sprites/bg.jpg')
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("RPG do SI")

    jogador = Personagem()

    jogando = True
    grupo_de_alvos = pygame.sprite.Group()

    for i in range(5):
        zumbi = Inimigo(random.randrange(0, largura), random.randrange(0, altura)) #só pode desenhar em grupos (conjunto)
        grupo_de_alvos.add(zumbi)

    while jogando:

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    jogador.rect.left -= jogador.velocidade

                if evento.key == pygame.K_RIGHT:
                    jogador.rect.right += jogador.velocidade

                if evento.key == pygame.K_DOWN:
                    jogador.rect.bottom += jogador.velocidade
                if evento.key == pygame.K_UP:
                    jogador.rect.top -= jogador.velocidade

        tela.blit(imagemFundo, (0, 0))
        grupo_de_alvos.draw(tela)
        jogador.colocar(tela)
        pygame.display.update()

        pygame.display.flip()
        clock.tick(60)


rpg()
