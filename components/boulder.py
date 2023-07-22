from components.power.node import BlockNode
from utils import grid_height, grid_width, index_to_coordinates
import pygame

class Boulder(pygame.sprite.Sprite,BlockNode):
    def __init__(self, position:tuple[int, int]):
        pygame.sprite.Sprite.__init__(self)
        BlockNode.__init__(self,position)

        self.base_image = pygame.image.load("assets/images/boulder.png")
        self.image = pygame.transform.scale(self.base_image,(800/grid_width,600/grid_height))
        #self.actual_image = pygame.transform.rotate(self.actual_image, randint(0,45))
    
    def draw(self, screen: pygame.Surface):
        self.resize(screen)
        self.rect = self.image.get_rect()
        self.rect.center = index_to_coordinates(screen, *self.position)
        screen.blit(self.image, self.rect)
	
    def resize(self, screen: pygame.Surface):
        self.image = pygame.transform.scale(self.base_image, (screen.get_width()/grid_width, screen.get_height()/grid_height))
