import pygame as pg


class Bird(pg.sprite.Sprite):
    GRAVITY = 900
    JUMP_STRENGTH = -250

    def __init__(self, screen, settings, *groups):
        """"""
        super().__init__(*groups)
        self.screen = screen
        self.settings = settings

        self.frames = [
            pg.image.load("assets/bird/redbird-downflap.png").convert_alpha(),
            pg.image.load("assets/bird/redbird-midflap.png").convert_alpha(),
            pg.image.load("assets/bird/redbird-upflap.png").convert_alpha(),
        ]
        self.frame_index = 0

        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center=(30, self.settings.height / 2))

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
