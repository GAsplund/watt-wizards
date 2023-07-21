import pygame


class PowerPole(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def getPosition(self):
        return self.rect.center
    
    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, self.rect)
    