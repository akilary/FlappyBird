import pygame as pg


class Pipe(pg.sprite.Sprite):
    MOVEMENT_SPEED = 220

    def __init__(self, screen, config, offset: int, *groups):
        super().__init__(*groups)
        self.screen = screen
        self.cfg = config
        self.image = self.load_image()
        self.rect = self.image.get_rect()

        gap = 120
        x, y = self.cfg.width, int(self.cfg.height / 2) + offset # Использовать Vector2
        self.set_position(x, y, gap)

    def load_image(self) -> pg.Surface:
        """Переопределяется в дочерних классах для разных ориентаций."""
        raise NotImplementedError("Метод load_image должен быть переопределен в дочернем классе.")

    def set_position(self, x: int, y: int, gap: int) -> None:
        """Переопределяется в дочерних классах для разных позиций."""
        raise NotImplementedError("Метод set_position должен быть переопределен в дочернем классе.")

    def update(self, dt: float) -> None:
        self.rect.x -= self.MOVEMENT_SPEED * dt
        if self.rect.right < 0:
            self.kill()
        self._draw()

    def _draw(self) -> None:
        self.screen.blit(self.image, self.rect)


class UpPipe(Pipe):
    def load_image(self):
        """Загружает изображение трубы."""
        return pg.transform.flip(pg.image.load("assets/obstacles/pipe-green.png").convert(), False, True)

    def set_position(self, x, y, gap):
        """Устанавливает позицию трубы."""
        self.rect.bottomleft = (x, y - int(gap / 2))


class DownPipe(Pipe):
    def load_image(self):
        """Загружает изображение трубы."""
        return pg.image.load("assets/obstacles/pipe-green.png").convert()

    def set_position(self, x, y, gap):
        """Устанавливает позицию трубы."""
        self.rect.topleft = (x, y + int(gap / 2))
