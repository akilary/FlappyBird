import sys, time
import pygame as pg
from random import randint

from core import Configs, Bird, Base, UpPipe, DownPipe, UI, GameState
from resource_utils import read_json, write_json
from resource_utils import load_image
from resource_utils import load_sound


class Game:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()

        self.cfg = Configs()
        self.screen = pg.display.set_mode((self.cfg.width, self.cfg.height))
        pg.display.set_caption("Flappy Clone")
        pg.display.set_icon(pg.image.load("assets/favicon.ico"))
        self.background_image = load_image("assets/environment/background.png")
        self.background_image = pg.transform.scale(self.background_image, (self.cfg.width, self.cfg.height))

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

        self.processed_pipes = []
        self.current_score = 0
        self.best_score = read_json("data/best_score.json")["best_score"]

        self.point_sound = load_sound("assets/audio/point.wav")
        self.hit_sound = load_sound("assets/audio/hit.wav")
        self.swoosh_sound = load_sound("assets/audio/swoosh.wav")

    def run(self) -> None:
        """Основной цикл игры: обработка событий, обновление объектов и отрисовка экрана."""
        last_time = time.time()
        while True:
            self.screen.blit(self.background_image, (0, 0))

            dt = time.time() - last_time
            last_time = time.time()

            self._check_events()
            match self.game_state:
                case GameState.RUNNING:
                    self.pipe_sprite.update(dt)
                    self.bird_sprite.update(dt)
                    self._collisions()
                    self.ui.display_score(len(self.processed_pipes))
                case GameState.MENU:
                    self.ui.display_menu(self.current_score, self.best_score)
            self.base_sprite.update(dt)

            pg.display.update()
            self.clock.tick(self.cfg.fps)

    def _check_events(self) -> None:
        """Обработка пользовательских событий."""
        for event in pg.event.get():
            quit_event = (event.type == pg.KEYDOWN and event.key == pg.K_q) or event.type == pg.QUIT
            if quit_event:
                pg.quit()
                sys.exit()

            is_action = (event.type == pg.KEYDOWN and event.key == pg.K_SPACE) or event.type == pg.MOUSEBUTTONDOWN
            match self.game_state:
                case GameState.RUNNING:
                    if is_action: self.bird.jump()
                case GameState.MENU:
                    if is_action:
                        self.game_state = GameState.RUNNING
                        self.swoosh_sound.play()

            if event.type == self.pipe_timer and self.game_state == GameState.RUNNING:
                offset = randint(-110, 110)
                UpPipe(self.screen, self.cfg, offset, self.pipe_sprite, self.collision_sprites)
                DownPipe(self.screen, self.cfg, offset, self.pipe_sprite, self.collision_sprites)

    def _collisions(self) -> None:
        """Обработка столкновений птицы с препятствиями и подсчет очков."""
        if pg.sprite.spritecollide(self.bird, self.collision_sprites, False): # type: ignore
            self.hit_sound.play()
            self.game_state = GameState.MENU
            self.bird_alive = False
            self._reset_game()

        if self.pipe_sprite:
            first_pipe = self.pipe_sprite.sprites()[0]
            if first_pipe not in self.processed_pipes and first_pipe.rect.right < self.bird.rect.left:
                self.point_sound.play()
                self.processed_pipes.append(first_pipe)

    def _reset_game(self) -> None:
        """Сброс игры после завершения: очистка объектов и обновление рекордов."""
        self.base_sprite.empty()
        self.pipe_sprite.empty()
        self.collision_sprites.empty()

        Base(self.screen, self.cfg, self.base_sprite, self.collision_sprites)
        self.bird.set_center()

        self.current_score = len(self.processed_pipes)
        self.processed_pipes.clear()
        if self.current_score > self.best_score:
            new_best_score = {"best_score": self.current_score}
            self.best_score = new_best_score["best_score"]
            write_json("data/best_score.json", new_best_score)
        self.score = 0


if __name__ == '__main__':
    game = Game()
    game.run()
