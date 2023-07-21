import pygame

from components.buildings.house import House
from components.power.grid import PowerGrid
from components.power.pole import PowerPole
from utils import grid_height, grid_width


class PowerMap:
    def __init__(self, background_image: pygame.Surface, screen: pygame.Surface):
        self.grid = PowerGrid()
        self.background_image = background_image
        self.screen = screen
        self.houses = []

    def draw_background(self):
        # TODO: Implement grid drawing code here
        block_width=int(self.screen.get_width()/grid_width)
        block_height=int(self.screen.get_height()/grid_height)
        self.background_image = pygame.transform.scale(self.background_image, (block_width, block_height))
        for x in range(0, self.screen.get_width(), block_width):
            for y in range(0, self.screen.get_height()-block_width,block_height ):
                self.screen.blit(self.background_image, (x, y))

    def draw(self):
        self.draw_background()
        for house in self.houses:
            house.draw(self.screen)
        self.grid.draw(self.screen) 
    
    def add_pole(self, pole):
        self.grid.add_power_pole(pole)
    
    def add_houses(self, houses: list[House]):
        self.houses = self.houses + houses
    
    def add_connection(self, start: PowerPole, end: PowerPole):
        self.grid.add_connection(start, end)
    
    def remove_pole_at(self,pos: tuple[int,int]):
        self.grid.remove_pole_at(pos)

    def get_pole_at(self,pos:tuple[int,int]):
        return self.grid.get_pole_at(pos)
    