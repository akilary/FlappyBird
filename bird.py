import pygame as pg


class Bird:
    GRAVITY = 700
    JUMP_STRENGTH = -250

    def __init__(self, screen, settings):
        """"""
        self.screen = screen
        self.settings = settings

        self.frames = [
            pg.image.load("assets/bird/redbird-downflap.png").convert_alpha(),
            pg.image.load("assets/bird/redbird-midflap.png").convert_alpha(),
            pg.image.load("assets/bird/redbird-upflap.png").convert_alpha(),
        ]
        self.frame_index = 0

        x, y = self.settings.width / 30, self.settings.height / 2
        self.pos = pg.math.Vector2(x, y)
        self.velocity_y = 0

        self.rect = self.frames[self.frame_index].get_rect()

    def update(self, dt: float) -> None:
        """"""
        self._update_position(dt)
        image = self._animate(dt)
        self._draw(image)

    def jump(self) -> None:
        """"""
        self.velocity_y = self.JUMP_STRENGTH

    def _update_position(self, dt: float) -> None:
        """"""
        self.velocity_y += self.GRAVITY * dt
        self.pos.y += self.velocity_y * dt
        self.rect.y = round(self.pos.y)

    def _animate(self, dt: float) -> pg.Surface:
        """"""
        self.frame_index += 10 * dt
        image = self.frames[int(self.frame_index) % len(self.frames)]
        rotated_image = pg.transform.rotate(image, -self.velocity_y * 0.1)
        return rotated_image

    def _draw(self, image: pg.Surface) -> None:
        """"""
        self.screen.blit(image, (self.pos.x, self.pos.y))
