# Автор ассетов: https://github.com/samuelcust/flappy-bird-assets.git
# Используется с разрешения автора

import sys, time
import pygame as pg
from random import randint

from core import Bird, Base, UpPipe, DownPipe
from utils import Configs, load_image


class Game:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()

        self.cfg = Configs()
        self.screen = pg.display.set_mode((self.cfg.width, self.cfg.height))
        pg.display.set_caption("Flappy Bird")
        self.background = self.cfg.load_background()

        self.all_sprites = pg.sprite.LayeredUpdates()
        self.collision_sprites = pg.sprite.Group()
        self.pipes = pg.sprite.Group()

        Base(self.screen, self.cfg, self.all_sprites, self.collision_sprites)
        self.bird = Bird(self.screen, self.cfg, self.all_sprites)

        self.pipe_timer = pg.USEREVENT + 1
        pg.time.set_timer(self.pipe_timer, 1000)

        self.last_passed_pipe = None
        self.score = 0

        self.game_state = "game_running"
        self.game_over_screen = load_image("assets/ui/gameover.png")

    def run(self) -> None:
        """"""
        last_time = time.time()
        while True:
            self.screen.blit(self.background, (0, 0))
            self._check_events()
            dt = time.time() - last_time
            last_time = time.time()
            self.all_sprites.update(dt)

            match self.game_state:
                case "game_running":
                    self._collisions()
                case "game_over":
                    self.screen.blit(self.game_over_screen, (0, 0))

            pg.display.update()
            self.clock.tick(self.cfg.fps)

    def _check_events(self) -> None:
        """"""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                match self.game_state:
                    case "game_running":
                        self.bird.jump()
                    case "game_over":
                        self.game_state = "game_running"
            if event.type == self.pipe_timer:
                offset = randint(-100, 100)
                UpPipe(self.screen, self.cfg, offset, self.all_sprites, self.pipes, self.collision_sprites)
                DownPipe(self.screen, self.cfg, offset, self.all_sprites, self.pipes, self.collision_sprites)


    def _collisions(self) -> None:
        """"""
        if pg.sprite.spritecollide(self.bird, self.collision_sprites, False): # type: ignore
            self.game_state = "game_over"

        for pipe in filter(lambda p: isinstance(p, UpPipe) and p.rect.centerx < self.bird.rect.centerx,
                           self.pipes):
            if self.last_passed_pipe != pipe:
                self.score += 1
                self.last_passed_pipe = pipe
                print("Score: ", self.score)



if __name__ == '__main__':
    game = Game()
    game.run()

