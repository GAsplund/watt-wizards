import pygame

from components.buildings.house import House
from components.power.grid import PowerGrid
from components.power.node import PowerNode
from utils import grid_height, grid_width


class PowerMap:
    def __init__(self, background_image: pygame.Surface, screen: pygame.Surface):
        self.grid = PowerGrid()
        self.background_image = background_image
        self.screen = screen
        self.resize_image(screen)

    def draw_background(self):
        block_width=int(self.screen.get_width()/grid_width)
        block_height=int(self.screen.get_height()/grid_height)
        for x in range(0, self.screen.get_width(), block_width):
            for y in range(0, self.screen.get_height()-block_width,block_height ):
                self.screen.blit(self.image, (x, y))

    def resize_image(self,screen:pygame.Surface):
        self.image = pygame.transform.scale(self.background_image, (screen.get_width()/grid_width, screen.get_height()/grid_height))
        self.grid.resize(screen)

    def draw(self):
        self.draw_background()
        self.grid.draw(self.screen) 
    
    def add_node(self, node: PowerNode):
        self.grid.add_power_node(node)

    def add_connection(self, start: PowerNode, end: PowerNode):
        self.grid.add_connection(start, end)
    
    def remove_node_at(self,pos: tuple[int,int]):
        self.grid.remove_node_at(pos)

    def get_node_at(self,pos:tuple[int,int]):
        return self.grid.get_node_at(pos)
    def win_condition_met(self):
        return self.grid.win_condition_met()
    