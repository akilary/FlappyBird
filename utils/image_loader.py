import pygame as pg


def load_image(path: str) -> pg.Surface:
    """"""
    img = pg.image.load(path)
    return img.convert_alpha()

def load_background(path: str) -> pg.Surface:
    """"""
    img = pg.image.load(path)
    return img.convert()
