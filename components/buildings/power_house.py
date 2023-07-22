import pygame

from components.buildings.house import House
from utils import *


class PowerHouse(House):
	def __init__(self, position:tuple[int,int]):
		super().__init__(position)
		self.base_image = pygame.image.load("assets/images/powerhouse.png")
		self.image = pygame.transform.scale(self.base_image,(800/grid_width,600/grid_height))
		self.remaining_power=15
		self.font = pygame.font.Font("assets/fonts/Planewalker.otf", 16)
    
	def is_conductive(self):
		return True

	def is_destructible(self):
		return False
	
	def get_power(self):
		return 15
	
	def set_remaining_power(self, power):
		self.remaining_power = power

	def draw(self, screen: pygame.Surface):
		super().draw(screen)
		text = f"Re: {self.remaining_power}, Tot: {15}"
		text_surface = self.font.render(text, True, (200, 200, 200))
		rect = text_surface.get_rect(center=index_to_coordinates(screen, self.position[0], self.position[1]))
		pygame.draw.rect(screen, (0,0,0), rect)
		screen.blit(text_surface, rect)

		