from pygame.mixer import Sound


def load_sound(path: str) -> Sound:
    """Загружает звуковой файл."""
    sound = Sound(path)
    return sound
