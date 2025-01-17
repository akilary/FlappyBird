import pygame as pg
from resource_utils import load_image


class Pipe(pg.sprite.Sprite):
    """Базовый класс трубы, отвечающий за общую логику движения и отрисовки."""
    MOVEMENT_SPEED = 270
    FILE_PATH = "assets/obstacles/pipe-green.png"

    def __init__(self, screen: pg.Surface, configs, offset: int, *groups):
        super().__init__(*groups)
        self.screen = screen
        self.cfg = configs
        self.image = self._load_image()
        self.rect = self.image.get_rect()

        gap = 120
        self.pos = pg.math.Vector2(self.cfg.width, int(self.cfg.height / 2) + offset)
        self._set_position(gap)

    def _load_image(self) -> pg.Surface:
        """Загружает изображение трубы. Переопределяется в дочерних классах."""
        raise NotImplementedError("Метод load_image должен быть переопределен в дочернем классе.")

    def _set_position(self, gap: int) -> None:
        """Устанавливает позицию трубы. Переопределяется в дочерних классах."""
        raise NotImplementedError("Метод set_position должен быть переопределен в дочернем классе.")

    def update(self, dt: float) -> None:
        """Обновляет позицию трубы и удаляет её, если она выходит за экран."""
        self.pos.x -= self.MOVEMENT_SPEED * dt
        if self.rect.right < 0: self.kill()
        self.rect.x = round(self.pos.x)
        self._draw()

    def _draw(self) -> None:
        self.screen.blit(self.image, self.rect)


class UpPipe(Pipe):
    def _load_image(self):
        """Загружает изображение и переворачивает его вверх ногами."""
        return pg.transform.flip(load_image(self.FILE_PATH), False, True)

    def _set_position(self, gap):
        """Устанавливает позицию трубы выше зазора."""
        x, y = round(self.pos.x), round(self.pos.y)
        self.rect.bottomleft = (x, y - int(gap / 2))


class DownPipe(Pipe):
    def _load_image(self):
        """Загружает изображение трубы без изменений."""
        return load_image(self.FILE_PATH)

    def _set_position(self, gap):
        """Устанавливает позицию трубы ниже зазора."""
        x, y = round(self.pos.x), round(self.pos.y)
        self.rect.topleft = (x, y + int(gap / 2))
