from pygame import image, Surface


def load_image(path: str) -> Surface:
    """Загружает изображение."""
    img = image.load(path)
    return img.convert_alpha()
