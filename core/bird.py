import pygame as pg
from resource_utils import load_image, load_sound


class Bird(pg.sprite.Sprite):
    GRAVITY = 1300
    JUMP_STRENGTH = -320

    def __init__(self, screen: pg.Surface, configs, *groups):
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

        self.wing_sound = load_sound("assets/audio/wing.wav")

    def update(self, dt: float) -> None:
        """Обновляет состояние птицы."""
        self._update_position(dt)
        self._animate(dt)
        self._draw()

    def jump(self) -> None:
        """Заставляет птицу прыгнуть."""
        self.velocity_y = self.JUMP_STRENGTH
        self.wing_sound.play()

    def set_center(self) -> None:
        """Сбрасывает положение птицы в центр экрана."""
        self.rect = self.image.get_rect(center=(30, self.cfg.height / 2))
        self.pos = pg.math.Vector2(self.rect.center)
        self.velocity_y = 0

    def _update_position(self, dt: float) -> None:
        """Обновляет позицию птицы с учётом гравитации."""
        self.velocity_y += self.GRAVITY * dt
        self.pos.y += self.velocity_y * dt
        self.rect.y = round(self.pos.y)

    def _animate(self, dt: float) -> None:
        """Анимирует движения птицы."""
        self.frame_index += 10 * dt
        new_frame = self.frames[int(self.frame_index) % len(self.frames)]
        rotated_image = pg.transform.rotate(new_frame, -self.velocity_y * 0.1)
        self.image = rotated_image

    def _draw(self) -> None:
        """Отрисовывает птицу на экране."""
        self.screen.blit(self.image, self.rect)
