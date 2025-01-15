# Автор ассетов: https://github.com/samuelcust/flappy-bird-assets.git
# Используется с разрешения автора

import sys, time
import pygame as pg
from random import randint

from core import Configs, Bird, Base, UpPipe, DownPipe, UI, GameState
from utils import load_background_image, read_json, write_json


class Game:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()

        self.cfg = Configs()
        self.screen = pg.display.set_mode((self.cfg.width, self.cfg.height))
        pg.display.set_caption("Flappy Clone")
        self.background_image = load_background_image(self.cfg)

        self.game_state = GameState.MENU

        self.bird_sprite = pg.sprite.GroupSingle()
        self.base_sprite = pg.sprite.GroupSingle()
        self.pipe_sprite = pg.sprite.Group()
        self.collision_sprites = pg.sprite.Group()

        Base(self.screen, self.cfg, self.base_sprite, self.collision_sprites)
        self.bird = Bird(self.screen, self.cfg, self.bird_sprite)

        self.ui = UI(self.screen, self.cfg)

        self.pipe_timer = pg.USEREVENT + 1
        pg.time.set_timer(self.pipe_timer, 1000)

        self.last_passed_pipe = None
        self.current_score = self.score = 0
        self.best_score = read_json("data/best_score.json")["best_score"]

    def run(self) -> None:
        """"""
        last_time = time.time()
        while True:
            self.screen.blit(self.background_image, (0, 0))

            dt = time.time() - last_time
            last_time = time.time()

            self._check_events()
            match self.game_state:
                case GameState.RUNNING:
                    self.bird_sprite.update(dt)
                    self.pipe_sprite.update(dt)
                    self._collisions()
                    self.ui.display_score(self.score)
                case GameState.MENU:
                    self.ui.display_menu(self.current_score, self.best_score)
            self.base_sprite.update(dt)

            pg.display.update()
            self.clock.tick(self.cfg.fps)

    def _check_events(self) -> None:
        """"""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            match self.game_state:
                case GameState.RUNNING:
                    if event.type == pg.MOUSEBUTTONDOWN: self.bird.jump()
                case GameState.MENU:
                    if event.type == pg.MOUSEBUTTONDOWN: self.game_state = GameState.RUNNING

            if event.type == self.pipe_timer and self.game_state == GameState.RUNNING:
                offset = randint(-110, 110)
                UpPipe(self.screen, self.cfg, offset, self.pipe_sprite, self.collision_sprites)
                DownPipe(self.screen, self.cfg, offset, self.pipe_sprite, self.collision_sprites)

    def _collisions(self) -> None:
        """"""
        if pg.sprite.spritecollide(self.bird, self.collision_sprites, False): # type: ignore
            self._reset_game()
            self.game_state = GameState.MENU

        for pipe in filter(lambda p: isinstance(p, UpPipe) and p.rect.centerx < self.bird.rect.centerx,
                           self.pipe_sprite):
            if self.last_passed_pipe != pipe:
                self.score += 1
                self.last_passed_pipe = pipe

    def _reset_game(self) -> None:
        """"""
        self.base_sprite.empty()
        self.pipe_sprite.empty()
        self.collision_sprites.empty()

        Base(self.screen, self.cfg, self.base_sprite, self.collision_sprites)
        self.bird.set_center()

        self.last_passed_pipe = None
        self.current_score = self.score
        if self.current_score > self.best_score:
            new_best_score = {"best_score": self.current_score}
            self.best_score = new_best_score["best_score"]
            write_json("data/best_score.json", new_best_score)
        self.score = 0


if __name__ == '__main__':
    game = Game()
    game.run()
