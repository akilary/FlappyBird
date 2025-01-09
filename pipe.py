import pygame as pg


class Pipe:
    MOVEMENT_SPEED = 220

    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings

        self.image = pg.image.load("assets/obstacles/pipe-green.png").convert()
        pipe_w, pipe_h = self.image.get_size()

        self.pos_top = pg.math.Vector2(self.settings.width, 0)
        self.pos_bottom = pg.math.Vector2(self.settings.width, self.settings.height-pipe_h)

    def new_pipe(self) -> None:
        """"""
        pass

    def update(self, dt) -> None:
        """"""
        self.pos_top.x -= self.MOVEMENT_SPEED * dt
        self.pos_bottom.x -= self.MOVEMENT_SPEED * dt
        self._draw()

    def _draw(self) -> None:
        """"""
        self.screen.blit(pg.transform.rotate(self.image, 180), (self.pos_top.x, self.pos_top.y))
        self.screen.blit(self.image, (self.pos_bottom.x, self.pos_bottom.y))


