import pygame

from components.power.pole import PowerPole


class PowerGrid:
    def __init__(self):
        self.graph: dict[tuple[int, int], list[tuple[int, int]]] = {}
        self.poles: dict[tuple[int, int], PowerPole] = {} 

    def add_power_pole(self, pole: PowerPole):
        self.poles[pole.getPosition()] = pole
        self.graph[pole.getPosition()] = []
        
    def add_connection(self, start: PowerPole, end: PowerPole):
        self.graph[start.getPosition()].append(end.getPosition())

    def get_neighbors(self, pole_id):
        return self.graph.get(pole_id, [])

    def draw(self, screen: pygame.Surface):
        for coords, pole in self.poles.items():
            pole.draw(screen)
            for neighbor in self.graph[coords]:
                self.__draw_connection(screen, coords, neighbor)
            

    def __draw_connection(self, screen: pygame.Surface,startPos: tuple[int, int], endPos: tuple[int,int]):
        pygame.draw.line(screen, (0, 0, 0), startPos, endPos, 2)