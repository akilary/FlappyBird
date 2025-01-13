# Автор ассетов: https://github.com/samuelcust/flappy-bird-assets.git
# Используется с разрешения автора

import sys, time
import pygame as pg
from random import randint

from core import Bird, Base, UpPipe, DownPipe, GameState
from utils import Configs, load_background_image, load_message_ui, load_gameover_ui


class Game:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()

        self.cfg = Configs()
        self.screen = pg.display.set_mode((self.cfg.width, self.cfg.height))
        pg.display.set_caption("Flappy Bird")

        self.background_image = load_background_image(self.cfg)
        self.message_ui, self.message_ui_rect = load_message_ui(self.cfg)
        self.game_over_ui, self.game_over_ui_rect = load_gameover_ui(self.cfg)

        self.game_state = GameState.MENU

        self.bird_sprite = pg.sprite.GroupSingle()
        self.base_sprite = pg.sprite.GroupSingle()
        self.pipe_sprite = pg.sprite.Group()
        self.collision_sprites = pg.sprite.Group()

        Base(self.screen, self.cfg, self.base_sprite, self.collision_sprites)
        self.bird = Bird(self.screen, self.cfg, self.bird_sprite)

        self.pipe_timer = pg.USEREVENT + 1
        pg.time.set_timer(self.pipe_timer, 1000)

        self.last_passed_pipe = None
        self.score = 0
        self.font = pg.font.Font("assets/font/Bungee-Regular.ttf", 36)

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
                    self._display_score()
                    self._collisions()
                case GameState.MENU:
                    self.screen.blit(self.message_ui, self.message_ui_rect)
                case GameState.GAME_OVER:
                    self.screen.blit(self.game_over_ui, self.game_over_ui_rect)
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
                case GameState.GAME_OVER:
                    if event.type == pg.MOUSEBUTTONDOWN: self.game_state = GameState.MENU

            if event.type == self.pipe_timer and self.game_state == GameState.RUNNING:
                offset = randint(-110, 110)
                UpPipe(self.screen, self.cfg, offset, self.pipe_sprite, self.collision_sprites)
                DownPipe(self.screen, self.cfg, offset, self.pipe_sprite, self.collision_sprites)

    def _collisions(self) -> None:
        """"""
        if pg.sprite.spritecollide(self.bird, self.collision_sprites, False): # type: ignore
            self._reset_game()
            self.game_state = GameState.GAME_OVER

        for pipe in filter(lambda p: isinstance(p, UpPipe) and p.rect.centerx < self.bird.rect.centerx,
                           self.pipe_sprite):
            if self.last_passed_pipe != pipe:
                self.score += 1
                self.last_passed_pipe = pipe

    def _display_score(self) -> None:
        """"""
        score_surf = self.font.render(f"{self.score}", True, (255, 255, 255))
        score_rect = score_surf.get_rect(center=(self.cfg.width/2, 40))
        self.screen.blit(score_surf, score_rect)

    def _reset_game(self) -> None:
        """"""
        self.base_sprite.empty()
        self.pipe_sprite.empty()
        self.collision_sprites.empty()

        Base(self.screen, self.cfg, self.base_sprite, self.collision_sprites)
        self.bird.set_center()

        self.last_passed_pipe = None
        self.score = 0


if __name__ == '__main__':
    game = Game()
    game.run()
