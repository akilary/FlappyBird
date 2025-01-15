import pygame as pg


class UI:
    def __init__(self, screen, configs):
        self.screen = screen
        self.cfg = configs

        self.title_font = pg.font.Font("assets/font/Bungee-Regular.ttf", 36)
        self.font = pg.font.Font("assets/font/Bungee-Regular.ttf", 28)

    def display_score(self, score) -> None:
        """"""
        score_surf = self.title_font.render(f"{score}", True, (255, 255, 255))
        score_rect = score_surf.get_rect(center=(self.cfg.width / 2, 40))
        self.screen.blit(score_surf, score_rect)

    def display_menu(self, score: int, best_score: int) -> None:
        """"""
        title_surf = self.title_font.render("Flappy Clone", True, (255, 255, 255))
        title_rect = title_surf.get_rect(center=(self.cfg.width / 2, 80))
        self.screen.blit(title_surf, title_rect)

        score_surf = self.font.render(f"Score: {score}", True, (255, 255, 255))
        score_rect = score_surf.get_rect(center=(self.cfg.width / 2, 200))
        self.screen.blit(score_surf, score_rect)

        best_score_surf = self.font.render(f"Best: {best_score}", True, (255, 255, 255))
        best_score_rect = best_score_surf.get_rect(center=(self.cfg.width / 2, 260))
        self.screen.blit(best_score_surf, best_score_rect)

        start_message_surf = self.font.render("Press SPACE or Click to Start", True, (255, 255, 255))
        start_message_rect = start_message_surf.get_rect(midbottom=(self.cfg.width / 2, self.cfg.height - 125))
        self.screen.blit(start_message_surf, start_message_rect)
