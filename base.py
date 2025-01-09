import pygame as pg


class Base:
    MOVEMENT_SPEED = 260

    def __init__(self, screen, settings):
        """"""
        self.screen = screen
        self.settings = settings

        self.image = pg.image.load("assets/environment/base.png").convert()
        self.rect = self.image.get_rect(bottomleft=(0,self.settings.height))

        self.pos = pg.math.Vector2(self.rect.topleft)

    def update(self, dt) -> None:
        """"""
        self.pos.x -= self.MOVEMENT_SPEED * dt
        if self.rect.centerx <= 0: self.pos.x = 0
        self.rect.x = round(self.pos.x)
        self._draw()

    def _draw(self) -> None:
        """"""
        self.screen.blit(self.image, (self.pos.x, self.pos.y))
        self.screen.blit(self.image, (self.pos.x + self.rect.width, self.pos.y))
