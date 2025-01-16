from datetime import datetime


class Configs:
    def __init__(self):
        self.fps = 120
        self.width = 500
        self.height = 700
        self.current_time = datetime.now().hour