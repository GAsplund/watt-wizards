# Description: Utility functions for the game
# from math import exp, expm1
import pygame

grid_width = 20
grid_height = 15
x_factor = lambda screen: screen.get_width() / grid_width
y_factor = lambda screen: screen.get_height() / grid_height
downsize = lambda screen, a, fun: int((a-0.5)/fun(screen))
upsize   = lambda screen, a, fun: int((a+0.5)*fun(screen))

def coordinates_to_index(screen: pygame.Surface, x: int, y: int):
	return (downsize(screen,x,x_factor),downsize(screen,y,y_factor))
	#return (int((x-0.5)/x_factor(screen,grid_width)),int((y-0.5)/y_factor(screen,grid_height)))
    
def index_to_coordinates(screen: pygame.Surface, x: int,y: int):
	return (upsize(screen,x,x_factor),upsize(screen,y,y_factor))
	#return (int((x+0.5)*x_factor(screen,grid_width)),int((y+0.5)*y_factor(screen,grid_height)))
