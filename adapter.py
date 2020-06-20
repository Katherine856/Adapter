import pygame
from pygame.sprite import Sprite
from pygame import *
import glob


class PersonajeAdaptado(Sprite):
    def __init__(self):
        super(PersonajeAdaptado, self).__init__()
        self.index = 0
        self.state = 0

    def set_sprites(self, sprites):
        self.sprites = sprites
        self.animar_state(self.state)

    def CDerecha(self):
        self.state = 1
        self.animar_state(self.state)

    def CIzquierda(self):
        self.state = 2
        self.animar_state(self.state)

    def dibujar(self, ventana):
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        self.index += 1

        ventana.blit(self.image, self.rect)

    def animar_state(self, action):
        im = glob.glob(self.sprites[action])
        lenim = len(im[0])
        self.images = [pygame.image.load(img)
                       for img in im if len(img) == lenim]
        self.images2 = [pygame.image.load(img)
                        for img in im if len(img) > lenim]
        self.images.extend(self.images2)
        self.rect = pygame.Rect(40, 40, 800, 600)



