import pygame

from components.power.node import PowerNode
from utils import grid_height, grid_width, index_to_coordinates


class PowerPole(pygame.sprite.Sprite, PowerNode):
    def __init__(self, position:tuple[int,int]):
        pygame.sprite.Sprite.__init__(self)
        PowerNode.__init__(self,position)
        self.base_image = pygame.image.load("assets/powerpole.png")
        self.image = pygame.transform.scale(self.base_image,(800,600))
        
    def is_conductive(self):
        return True

    
    def draw(self, screen: pygame.Surface):
        block_width=int(screen.get_width()/(grid_width*2))
        block_height=int(screen.get_height()/(grid_height*2))
        #image = pygame.transform.scale(self.actual_image, (block_width, block_height))
        self.rect = self.image.get_rect()
        self.rect.center = index_to_coordinates(screen, *self.position)
        screen.blit(self.image, self.rect)

    def resize_image(self, screen: pygame.Surface):
        self.image = pygame.transform.scale(self.base_image, (screen.get_width(), screen.get_height()))

    def is_destructible(self):
        return True
    