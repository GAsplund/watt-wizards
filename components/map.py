import pygame

from components.power.grid import PowerGrid
from components.power.node import PowerNode
from utils import grid_height, grid_width


class PowerMap:
    def __init__(self, background_image: pygame.Surface, screen: pygame.Surface):
        self.grid = PowerGrid()
        self.background_image = background_image
        self.screen = screen
        self.resize_image(screen)
        self.font = pygame.font.Font("assets/fonts/Planewalker.otf", 32)

    def draw_background(self):
        try:
            block_width = int(self.screen.get_width()/grid_width)
            block_height = int(self.screen.get_height()/grid_height)
            for x in range(0, self.screen.get_width(), block_width):
                for y in range(0, self.screen.get_height(),block_height ):
                    self.screen.blit(self.image, (x, y))
        except: pass
        
    def resize_image(self,screen:pygame.Surface):
        self.image = pygame.transform.scale(self.background_image, (screen.get_width()/grid_width, screen.get_height()/grid_height))
        self.grid.resize(screen)

    def draw(self):
        self.draw_background()
        self.draw_info()
        self.grid.draw(self.screen) 
    
    def add_node(self, node: PowerNode):
        node.resize(self.screen)
        self.grid.add_power_node(node)

    def draw_info(self):
        pygame.draw.rect(self.screen, (255, 105, 180), ((self.screen.get_width()/grid_width)*16,0, self.screen.get_width(), (self.screen.get_height()/grid_height)*2))
        text = f"Poles left: {self.grid.total_poles}"
        text_surface = self.font.render(text, True, (0, 0, 0))
        rect = text_surface.get_rect(center=((self.screen.get_width()/grid_width)*17, (self.screen.get_height()/grid_height)))
        self.screen.blit(text_surface, rect)

    def add_connection(self, start: PowerNode, end: PowerNode):
        self.grid.add_connection(start, end)
    
    def remove_node_at(self,pos: tuple[int,int]):
        self.grid.remove_node_at(pos)

    def get_node_at(self,pos:tuple[int,int]):
        return self.grid.get_node_at(pos)
    def win_condition_met(self):
        return self.grid.win_condition_met()

    def flush(self):
        self.grid = PowerGrid()
    