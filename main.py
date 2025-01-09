# Автор ассетов: https://github.com/samuelcust/flappy-bird-assets.git
# Используется с разрешения автора

import sys, time
import pygame as pg

from core import Bird, Base, Pipe
from utils import Configs


class Game:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()

        self.cfg = Configs()
        self.display_surface = pg.display.set_mode((self.cfg.width, self.cfg.height))
        pg.display.set_caption("Flappy Bird")
        self.background = self.cfg.load_background()

        self.all_sprites = pg.sprite.Group()
        self.collision_sprites = pg.sprite.Group()

        Base(self.display_surface, self.cfg, self.all_sprites, self.collision_sprites)
        self.bird = Bird(self.display_surface, self.cfg, self.all_sprites)

        self.pipe_timer = pg.USEREVENT + 1
        pg.time.set_timer(self.pipe_timer, 1000)

    def run(self) -> None:
        """"""
        last_time = time.time()
        while True:
            self.display_surface.blit(self.background, (0, 0))
            self._check_events()

            dt = time.time() - last_time
            last_time = time.time()

            self.all_sprites.update(dt)
            self._collisions()

            pg.display.update()
            self.clock.tick(self.cfg.fps)

    def _check_events(self) -> None:
        """"""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                self.bird.jump()
            if event.type == self.pipe_timer:
                print("create pipe")
                Pipe(self.display_surface, self.cfg, self.all_sprites, self.collision_sprites)

    def _collisions(self) -> None:
        """"""
        if pg.sprite.spritecollide(self.bird, self.collision_sprites, False): # type: ignore
            sys.exit()


if __name__ == '__main__':
    game = Game()
    game.run()
