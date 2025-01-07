import pygame as pg


class Bird:
    GRAVITY = 700
    JUMP_STRENGTH = -250

    def __init__(self, screen, settings):
        """"""
        self.screen = screen
        self.settings = settings

        self.frames = [
            pg.image.load("assets/bird/down_flap.png").convert_alpha(),
            pg.image.load("assets/bird/mid_flap.png").convert_alpha(),
            pg.image.load("assets/bird/up_flap.png").convert_alpha(),
        ]
        self.frame_index = 0

        self.x, self.y = self.settings.width / 20, self.settings.height / 2
        self.velocity_y = 0

        self.bird_width, self.bird_height = self.frames[self.frame_index].get_size()
        self.rect = pg.Rect(self.x, self.y, self.bird_width, self.bird_height)

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
        self.rect = pg.Rect(self.x, self.y, self.bird_width, self.bird_height)
        self.velocity_y += self.GRAVITY * dt
        self.y += self.velocity_y * dt

    def _animate(self, dt: float) -> pg.Surface:
        """"""
        self.frame_index += 10 * dt
        image = self.frames[int(self.frame_index) % len(self.frames)]
        rotated_image = pg.transform.rotate(image, -self.velocity_y * 0.1)
        return rotated_image

    def _draw(self, image: pg.Surface) -> None:
        """"""
        self.screen.blit(image, (self.x, self.y))
