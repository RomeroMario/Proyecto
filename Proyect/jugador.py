import pygame
from variables import *

# Clase para el jugador
class Player(pygame.sprite.Sprite):
    def __init__(self,size):
        super().__init__()
        imagen = pygame.image.load('player.png').convert_alpha()
        self.image = pygame.transform.scale(imagen, (size, size))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, (HEIGHT // 2) + 250)
        self.speed = 6

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_d] and self.rect.right < WIDTH:
            self.rect.x += self.speed
        if keys[pygame.K_w] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_s] and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed
