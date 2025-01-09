import pygame as pg


class Configs:
    def __init__(self):
        self.fps = 120
        self.width = 500
        self.height = 750

    def load_background(self) -> pg.Surface:
        """"""
        image = pg.image.load("assets/environment/background-day.png").convert()
        scaled_bg_image = pg.transform.scale(image, (self.width, self.height))
        return scaled_bg_image

