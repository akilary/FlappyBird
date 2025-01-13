import pygame as pg
from .image_loader import load_background

class Configs:
    def __init__(self):
        self.fps = 120
        self.width = 500
        self.height = 750


    def load_background(self) -> pg.Surface:
        """"""
        image = load_background("assets/environment/background-day.png")
        scaled_bg_image = pg.transform.scale(image, (self.width, self.height))
        return scaled_bg_image

