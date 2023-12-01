import pygame
import random
from variables import *

# Clase para el enemigo
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()
        imagen = pygame.image.load('enemigo.png').convert_alpha()
        self.image = pygame.transform.scale(imagen, (15, 60))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            #Al llegar abajo se elimina
            self.kill()
