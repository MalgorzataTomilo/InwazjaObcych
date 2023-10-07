import pygame.font

class Button():
    def __init__(self, ai_game, screen, msg):
        '''Inicjalizacja atrybutów przycisku'''
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        # Zdefiniowanie wymiarów i właściwości przycisku 
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        # Utworzenie prostokąta przycisku i wyśrodkowanie go 
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        # Komunikat wyświetlany przez przycisk 
        self._prep_msg(msg)
    
    def _prep_msg(self, msg):
        '''Umieszczenie kominikat i wyśrodkowanie tekstu na przycisku'''
        self.mgs_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.mgs_image_rect = self.mgs_image.get_rect()
        self.mgs_image_rect.center = self.rect.center


    
