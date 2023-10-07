import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''Klasa przeznaczona do zarządzania pociskami wystrzeliwanymi przez statek'''

    def __init__(self, ai_game):
        '''Utworzenie obiektu pocisku w aktualnym połozeniu statku'''
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings 
        self.color = self.settings.bullet_color

# Utworzenie prostokąta pocisku w punkcie (0,0), a następnie zdefiniowania dla niego odpowiedniego połozenia
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height) 
        self.rect.midtop = ai_game.ship.rect.midtop
# Połozenie pocisku 
        self.y = float(self.rect.y)

    def update(self):
        '''Poruszanie pociskiem po ekranie'''
# Uaktualnianie połozenia pocisku 
        self.y -=self.settings.bullet_speed
# Uaktualnianie połozenia prostokąta pocisku
        self.rect.y = self.y

    def draw_bullet(self):
        '''Wyświetlenie pocisku na ekranie'''
        pygame.draw.rect(self.screen, self.color, self.rect)