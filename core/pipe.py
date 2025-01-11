import pygame as pg


class Pipe(pg.sprite.Sprite):
    MOVEMENT_SPEED = 260
    FILE_PATH = "assets/obstacles/pipe-green.png"

    def __init__(self, screen, config, offset: int, *groups):
        super().__init__(*groups)
        self._assign_layer(groups)
        self.screen = screen
        self.cfg = config
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

    def update(self, dt: float) -> None:
        self.pos.x -= self.MOVEMENT_SPEED * dt
        if self.rect.right < 0: self.kill()
        self.rect.x = round(self.pos.x)
        self._draw()

    def _draw(self) -> None:
        self.screen.blit(self.image, self.rect)

    def _assign_layer(self, groups) -> None:
        """"""
        for group in groups:
            if isinstance(group, pg.sprite.LayeredUpdates):
                group.change_layer(self, -1) # type: ignore


class UpPipe(Pipe):
    def _load_image(self):
        """Загружает изображение трубы."""
        return pg.transform.flip(pg.image.load(self.FILE_PATH).convert(), False, True)

    def _set_position(self, gap):
        """Устанавливает позицию трубы."""
        x, y = round(self.pos.x), round(self.pos.y)
        self.rect.bottomleft = (x, y - int(gap / 2))


class DownPipe(Pipe):
    def _load_image(self):
        """Загружает изображение трубы."""
        return pg.image.load(self.FILE_PATH).convert()

    def _set_position(self, gap):
        """Устанавливает позицию трубы."""
        x, y = round(self.pos.x), round(self.pos.y)
        self.rect.topleft = (x, y + int(gap / 2))
