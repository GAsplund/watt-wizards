import pygame

from components.power.node import PowerNode
from utils import grid_height, grid_width, index_to_coordinates


class PowerPole(pygame.sprite.Sprite, PowerNode):
    def __init__(self, position:tuple[int,int]):
        pygame.sprite.Sprite.__init__(self)
        PowerNode.__init__(self,position)
        self.actual_image = pygame.image.load("assets/powerpole.png")
        
    def is_conductive(self):
        return True

    
    def draw(self, screen: pygame.Surface):
        block_width=int(screen.get_width()/(grid_width*2))
        block_height=int(screen.get_height()/(grid_height*2))
        image = pygame.transform.scale(self.actual_image, (block_width, block_height))
        self.rect = image.get_rect()
        self.rect.center = index_to_coordinates(screen, *self.position)
        screen.blit(image, self.rect)

    def is_destructible(self):
        return True
    