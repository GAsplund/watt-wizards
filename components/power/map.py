import pygame

from components.power.grid import PowerGrid


class PowerMap:
    def __init__(self, background_image: pygame.Surface, screen: pygame.Surface):
        self.grid = PowerGrid()
        self.background_image = background_image
        self.screen = screen

    def draw_background(self):
        # TODO: Implement grid drawing code here
        for x in range(0, self.screen.get_width(), self.background_image.get_width()):
            for y in range(0, self.screen.get_height(), self.background_image.get_height()):
                self.screen.blit(self.background_image, (x, y))

    def draw(self):
        self.draw_background()
        self.grid.draw(self.screen) 
    
    def add_pole(self, pole):
        self.grid.add_power_pole(pole)