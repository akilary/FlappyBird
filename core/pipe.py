import pygame as pg
from utils import load_image

class Pipe(pg.sprite.Sprite):
    MOVEMENT_SPEED = 270
    FILE_PATH = "assets/obstacles/pipe-green.png"

    def __init__(self, screen, configs, offset: int, *groups):
        super().__init__(*groups)
        self.screen = screen
        self.cfg = configs
        self.image = self._load_image()
        self.rect = self.image.get_rect()

        gap = 120
        self.pos = pg.math.Vector2(self.cfg.width, int(self.cfg.height / 2) + offset)
        self._set_position(gap)

    def _load_image(self) -> pg.Surface:
        """Переопределяется в дочерних классах для разных ориентаций."""
        raise NotImplementedError("Метод load_image должен быть переопределен в дочернем классе.")

    def _set_position(self, gap: int) -> None:
        """Переопределяется в дочерних классах для разных позиций."""
        raise NotImplementedError("Метод set_position должен быть переопределен в дочернем классе.")

    def update(self, dt: float, bird_alive: bool=True) -> None:
        if bird_alive:
            self.pos.x -= self.MOVEMENT_SPEED * dt
            if self.rect.right < 0: self.kill()
            self.rect.x = round(self.pos.x)
        self._draw()

    def _draw(self) -> None:
        self.screen.blit(self.image, self.rect)


class UpPipe(Pipe):
    def _load_image(self):
        """Загружает изображение трубы."""
        return pg.transform.flip(load_image(self.FILE_PATH), False, True)

    def _set_position(self, gap):
        """Устанавливает позицию трубы."""
        x, y = round(self.pos.x), round(self.pos.y)
        self.rect.bottomleft = (x, y - int(gap / 2))


class DownPipe(Pipe):
    def _load_image(self):
        """Загружает изображение трубы."""
        return load_image(self.FILE_PATH)

    def _set_position(self, gap):
        """Устанавливает позицию трубы."""
        x, y = round(self.pos.x), round(self.pos.y)
        self.rect.topleft = (x, y + int(gap / 2))
