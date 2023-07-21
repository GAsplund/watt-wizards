import pygame

from components.power.pole import PowerPole
from utils import index_to_coordinates


class PowerGrid:
    def __init__(self):
        self.graph: dict[tuple[int, int], list[tuple[int, int]]] = {}
        self.poles: dict[tuple[int, int], PowerPole] = {} 

    def add_power_pole(self, pole: PowerPole):
        if pole.getPosition() not in self.poles:
            self.poles[pole.getPosition()] = pole
            self.graph[pole.getPosition()] = []
        
    def add_connection(self, start: PowerPole, end: PowerPole):
        self.graph[start.getPosition()].append(end.getPosition())

    def draw(self, screen: pygame.Surface):
        self.__draw_poles(screen)
        self.__draw_connections(screen)
    
    def remove_pole_at(self,pos: tuple[int,int]):
        self.poles.pop(pos,None)
        self.graph.pop(pos,None)
    
    def get_pole_at(self,pos: tuple[int,int]):
        return self.poles.get(pos,None)

    @staticmethod
    def get_length(pole1, pole2):
        return ((pole1[0] - pole2[0])**2 + (pole1[1] - pole2[1])**2)**0.5

    def __draw_poles(self, screen):
        for pole in self.poles.values():
            pole.draw(screen)

    def __draw_connections(self, screen):
        for coords, neighbors in self.graph.items():
            for neighbor in neighbors:
                self.__draw_connection(screen, coords, neighbor)

    def __draw_connection(self, screen, coords, neighbor):
        pygame.draw.line(screen, self.__color, coords, neighbor)
            

    def __draw_connection(self, screen: pygame.Surface,startPos: tuple[int, int], endPos: tuple[int,int]):
        pygame.draw.line(screen, (0, 0, 0), index_to_coordinates(screen,*startPos), index_to_coordinates(screen, *endPos), 2)