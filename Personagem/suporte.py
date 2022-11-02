from os import walk
import pygame

def pasta(caminho):

    lista_surfaces = []


    for _,__, img_files in walk(caminho):
        for image in img_files:
            caminho_completo = caminho +'/'+ image
            image_surface = pygame.image.load(caminho_completo).convert_alpha()
            lista_surfaces.append(image_surface)

    return lista_surfaces