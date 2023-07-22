import pygame

from components.power.node import PowerNode
from utils import grid_height, grid_width, index_to_coordinates


class PowerPole(pygame.sprite.Sprite, PowerNode):
    def __init__(self, position:tuple[int,int]):
        pygame.sprite.Sprite.__init__(self)
        PowerNode.__init__(self,position)
        self.base_image = pygame.image.load("assets/images/powerpole.png")
        self.image = pygame.transform.scale(self.base_image,(800/grid_width,600/grid_height))
        self.power = 0
        
    def is_conductive(self):
        return True
    
    def set_power(self, power:int):
        self.power = power

    
    def draw(self, screen: pygame.Surface):
        self.resize(screen)
        surface = pygame.Surface(self.image.get_size(),pygame.SRCALPHA)
        surface.fill((255,0,0,(self.power/15)*255))
        
        
        self.erect = self.image.get_rect()
        self.erect.center = index_to_coordinates(screen, *self.position)
        screen.blit(self.image, self.erect)
        screen.blit(surface, self.erect)

    def resize(self, screen: pygame.Surface):
        self.image = pygame.transform.scale(self.base_image, (screen.get_width()/grid_width, screen.get_height()/grid_height))

    def is_destructible(self):
        return True
