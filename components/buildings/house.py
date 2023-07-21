import pygame

from utils import *


class House(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()
		self.position = (x,y)
		self.image = pygame.image.load("assets/house.png")
        

	def getPosition(self):
		return self.position
    
	def draw(self, screen: pygame.Surface):
		block_width=int(screen.get_width()/grid_width)
		block_height=int(screen.get_height()/grid_height)
		self.image = pygame.transform.scale(self.image, (block_width, block_height))
		self.rect = self.image.get_rect()
		self.rect.center = index_to_coordinates(screen, *self.position)
		screen.blit(self.image, self.rect)
    
        