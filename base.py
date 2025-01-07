import pygame as pg


class Base:
    MOVEMENT_SPEED = 260

    def __init__(self, screen, settings):
        """"""
        self.screen = screen
        self.settings = settings

        self.image = pg.image.load("assets/environment/base.png").convert()
        self.image = pg.transform.rotozoom(self.image, 0, 1.2)
        self.rect = self.image.get_rect()
        self.rect.y = self.settings.height - self.rect.height

        self.x = 0

    def update(self, dt) -> None:
        """"""
        self.x -= self.MOVEMENT_SPEED * dt
        if self.x <= -self.rect.width // 2:
            self.x = 0
        self._draw()

    def _draw(self) -> None:
        """"""
        self.screen.blit(self.image, (self.x, self.rect.y))
        self.screen.blit(self.image, (self.x + self.rect.width, self.rect.y))
