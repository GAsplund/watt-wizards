import pygame

from components.buildings.house import House
from utils import *


class PowerHouse(House):
	def __init__(self, position:tuple[int,int]):
		super().__init__(position)
		self.base_image = pygame.image.load("assets/powerhouse.png")
		self.image = pygame.transform.scale(self.base_image,(800/grid_width,600/grid_height))
    
	def is_conductive(self):
		return True

	def is_destructible(self):
		return False
	
	def get_power(self):
		return 15