# -*- coding: utf-8 -*-
"""
Projet jeu 1 affichage chiffre
"""

import pygame
import random
from pygame.locals import *

pygame.init()

#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((640, 480))

# choix d'un fond de couleur 
numero_fond = random.randint(1,4)
if numero_fond == 1:
    #Chargement et collage du fond
    fond = pygame.image.load("fondrouge.jpg").convert()

elif numero_fond == 2:
    fond = pygame.image.load("fondbleu.jpg").convert()

elif numero_fond == 3:
    fond = pygame.image.load("fondviolet.jpg").convert()

else:
    fond = pygame.image.load("fondvert.jpg").convert()

fenetre.blit(fond, (0,0))

#Rafraîchissement de l'écran
pygame.display.flip()

