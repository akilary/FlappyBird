from pygame import image, transform, Surface


def load_image(path: str) -> Surface:
    """"""
    img = image.load(path)
    return img.convert_alpha()


def load_background_image(cfg) -> Surface:
    """"""
    img = image.load("assets/environment/background-day.png").convert()
    scaled_img = transform.scale(img, (cfg.width, cfg.height))
    return scaled_img

