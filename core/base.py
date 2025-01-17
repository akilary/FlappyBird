import pygame as pg
from resource_utils import load_image


class Base(pg.sprite.Sprite):
    MOVEMENT_SPEED = 270

    def __init__(self, screen: pg.Surface, configs, *groups):
        """"""
        super().__init__(*groups)
        self.screen = screen
        self.cfg = configs

        self.image = load_image("assets/environment/base.png")
        self.rect = self.image.get_rect(bottomleft=(0,self.cfg.height))

        self.pos = pg.math.Vector2(self.rect.topleft)

    def update(self, dt, bird_alive: bool=True) -> None:
        """Обновляет положение земли и циклично прокручивает её."""
        if bird_alive:
            self.pos.x -= self.MOVEMENT_SPEED * dt
            if self.pos.x <= -120: self.pos.x = 0
            self.rect.x = round(self.pos.x)
        self._draw()

    def _draw(self) -> None:
        """Отрисовывает землю на экране, создавая эффект прокрутки."""
        self.screen.blit(self.image, (self.pos.x, self.pos.y))
