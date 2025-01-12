import pygame as pg


class Base(pg.sprite.Sprite):
    MOVEMENT_SPEED = 270

    def __init__(self, screen, config, *groups):
        """"""
        super().__init__(*groups)
        self.screen = screen
        self.cfg = config

        self.image = pg.image.load("assets/environment/base.png").convert()
        self.rect = self.image.get_rect(bottomleft=(0,self.cfg.height))

        self.pos = pg.math.Vector2(self.rect.topleft)
        self.half_width = self.rect.centerx

    def update(self, dt) -> None:
        """"""
        self.pos.x -= self.MOVEMENT_SPEED * dt
        if abs(self.pos.x) >= self.half_width: self.pos.x = 0
        self.rect.x = round(self.pos.x)
        self._draw()

    def _draw(self) -> None:
        """"""
        self.screen.blit(self.image, (self.pos.x, self.pos.y))
        self.screen.blit(self.image, (self.pos.x + self.rect.width, self.pos.y))
