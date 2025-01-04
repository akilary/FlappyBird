import pygame as pg


class Base(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("assets/environment/base.png").convert()
        self.rect = self.image.get_rect()
