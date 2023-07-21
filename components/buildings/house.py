from random import randint

import pygame

from components.power.endpoint import PowerEndpoint
from utils import *


class House(pygame.sprite.Sprite, PowerEndpoint):
	def __init__(self, position:tuple[int, int]):
		pygame.sprite.Sprite.__init__(self)
		PowerEndpoint.__init__(self,position)
		
		self.actual_image = pygame.image.load("assets/house.png")
		self.actual_image = pygame.transform.rotate(self.actual_image, randint(0,45))
    
	def draw(self, screen: pygame.Surface):
		block_width = int(screen.get_width()/grid_width)
		block_height = int(screen.get_height()/grid_height)
		image = pygame.transform.scale(self.actual_image, (block_width, block_height))
		self.rect = image.get_rect()
		self.rect.center = index_to_coordinates(screen, *self.position)
		screen.blit(image, self.rect)

	def is_conductive(self):
		return False
	def get_power(self):
		return -3
	def is_destructible(self):
		return False