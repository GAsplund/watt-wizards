from random import randint

import pygame

from components.power.endpoint import PowerEndpoint
from utils import *


class House(pygame.sprite.Sprite, PowerEndpoint):
	def __init__(self, position:tuple[int, int]):
		pygame.sprite.Sprite.__init__(self)
		PowerEndpoint.__init__(self,position)
		
		self.base_image = pygame.image.load("assets/house.png")
		self.image = pygame.transform.scale(self.base_image,(800,600))
		#self.actual_image = pygame.transform.rotate(self.actual_image, randint(0,45))
    
	def draw(self, screen: pygame.Surface):
		block_width = int(screen.get_width()/grid_width)
		block_height = int(screen.get_height()/grid_height)
		self.rect = self.image.get_rect()
		self.rect.center = index_to_coordinates(screen, *self.position)
		screen.blit(self.image, self.rect)
	
	def resize_image(self, screen: pygame.Surface):
		self.image = pygame.transform.scale(self.base_image, (screen.get_width(), screen.get_height()))

	def is_conductive(self):
		return False
	def get_power(self):
		return -3
	def is_destructible(self):
		return False