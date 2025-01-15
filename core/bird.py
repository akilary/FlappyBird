import pygame as pg

from utils import load_image


class Bird(pg.sprite.Sprite):
    GRAVITY = 1300
    JUMP_STRENGTH = -320

    def __init__(self, screen, configs, *groups):
        """"""
        super().__init__(*groups)
        self.screen = screen
        self.cfg = configs

        self.frames = [
            load_image("assets/bird/redbird-downflap.png"),
            load_image("assets/bird/redbird-midflap.png"),
            load_image("assets/bird/redbird-upflap.png"),
        ]
        self.frame_index = 0

        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center=(30, self.cfg.height / 2))

        self.pos = pg.math.Vector2(self.rect.center)
        self.velocity_y = 0

    def update(self, dt: float) -> None:
        """"""
        self._update_position(dt)
        self._animate(dt)
        self._draw()

    def jump(self) -> None:
        """"""
        self.velocity_y = self.JUMP_STRENGTH

    def set_center(self) -> None:
        """"""
        self.rect = self.image.get_rect(center=(30, self.cfg.height / 2))
        self.pos = pg.math.Vector2(self.rect.center)
        self.velocity_y = 0

    def _update_position(self, dt: float) -> None:
        """"""
        self.velocity_y += self.GRAVITY * dt
        self.pos.y += self.velocity_y * dt
        self.rect.y = round(self.pos.y)

    def _animate(self, dt: float) -> None:
        """"""
        self.frame_index += 10 * dt
        new_frame = self.frames[int(self.frame_index) % len(self.frames)]
        rotated_image = pg.transform.rotate(new_frame, -self.velocity_y * 0.1)
        self.image = rotated_image

    def _draw(self) -> None:
        """"""
        self.screen.blit(self.image, self.rect)
