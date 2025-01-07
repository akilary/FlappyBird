# Автор ассетов: https://github.com/samuelcust/flappy-bird-assets.git
# Используется с разрешения автора

import sys, time
import pygame as pg

from settings import Settings
from bird import Bird
from base import Base


class Game:
    def __init__(self):
        pg.init()
        self.settings = Settings()
        self.display_surface = pg.display.set_mode((self.settings.width, self.settings.height))
        pg.display.set_caption("Flappy Bird")
        self.background = self.settings.load_background()

        self.bird = Bird(self.display_surface, self.settings)
        self.base = Base(self.display_surface, self.settings)

        self.clock = pg.time.Clock()

    def run(self) -> None:
        """"""
        last_time = time.time()
        while True:
            self.display_surface.blit(self.background, (0, 0))
            self._check_events()

            dt = time.time() - last_time
            last_time = time.time()

            self.bird.update(dt)
            self.base.update(dt)
            self._collisions()

            pg.display.update()
            self.clock.tick(self.settings.fps)

    def _check_events(self) -> None:
        """"""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                self.bird.jump()

    def _collisions(self) -> None:
        """"""
        if self.bird.rect.colliderect(self.base.rect):
            sys.exit()


if __name__ == '__main__':
    game = Game()
    game.run()
