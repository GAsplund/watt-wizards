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
        self.font = pygame.font.Font("assets/fonts/Planewalker.otf", 16)

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
    
    def erect_pole(self, node: PowerNode):
        node.resize(self.screen)
        self.grid.add_power_node(node)

    def draw_info(self):
        text_row1 = f"Towers left: {self.grid.total_poles}"
        text_row2 = f"Towers used: {self.grid.max_poles - self.grid.total_poles}"
        text_surface_row_1 = self.font.render(text_row1, True, (0, 0, 0))
        text_surface_row_2 = self.font.render(text_row2, True, (0, 0, 0))
        rect_row_1 = text_surface_row_1.get_rect(topleft=(self.screen.get_width()-110, 10))
        rect_row_2 = text_surface_row_1.get_rect(topleft=(self.screen.get_width()-110,30))
        pygame.draw.rect(self.screen, (200,200,200), (self.screen.get_width()-120,0, 150, 60))
        self.screen.blit(text_surface_row_1, rect_row_1)
        self.screen.blit(text_surface_row_2, rect_row_2)

    def add_connection(self, start: PowerNode, end: PowerNode):
        return self.grid.add_connection(start, end)
    
    def remove_node_at(self,pos: tuple[int,int]):
        return self.grid.remove_node_at(pos)

    def get_node_at(self,pos:tuple[int,int]):
        return self.grid.get_node_at(pos)

    def win_condition_met(self):
        return self.grid.win_condition_met()
    
    def get_towers_used(self):
        return self.grid.get_towers_used()

    def flush(self):
        self.grid = PowerGrid()
    