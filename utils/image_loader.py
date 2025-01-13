import pygame as pg



def load_image(path: str) -> pg.Surface:
    """"""
    img = pg.image.load(path)
    return img.convert_alpha()


def load_background_image(cfg) -> pg.Surface:
    """"""
    image = pg.image.load("assets/environment/background-day.png").convert()
    scaled_bg_image = pg.transform.scale(image, (cfg.width, cfg.height))
    return scaled_bg_image


def load_message_ui(cfg) -> type[pg.Surface, pg.Surface]:
    """"""
    image = pg.image.load("assets/ui/message.png").convert_alpha()
    image_rect = image.get_rect(centerx=cfg.width / 2, centery=cfg.height / 2)
    return image, image_rect


def load_gameover_ui(cfg) -> type[pg.Surface, pg.Surface]:
    """"""
    image = pg.image.load("assets/ui/gameover.png").convert_alpha()
    image_rect = image.get_rect(centerx=cfg.width / 2, centery=100)
    return image, image_rect
