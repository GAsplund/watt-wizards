import pygame

from components.power.endpoint import PowerEndpoint
from components.power.node import PowerNode
from components.power.pole import PowerPole
from data_structures.undirected_graph import UndirectedGraph
from utils import index_to_coordinates


class PowerGrid:
    def __init__(self):
        self.graph = UndirectedGraph()
        self.nodes: dict[tuple[int, int], PowerNode] = {} 
        self.total_poles = 10
        self.power_houses = []
        self.drain_houses = []
        self.has_won = False

    def add_power_node(self, power_node: PowerNode):
        if power_node.get_position() not in self.nodes and self.total_poles > 0: 
            self.nodes[power_node.get_position()] = power_node 
            self.graph.add_vertex(power_node.get_position())
            self.total_poles -= 1

            if not isinstance(power_node, PowerEndpoint):
                return
            
            if power_node.get_power() > 0:
                self.power_houses.append(power_node)
            else:
                self.drain_houses.append(power_node)

    def add_connection(self, start: PowerNode, end: PowerNode):
        if PowerGrid.get_length(start.get_position(), end.get_position()) > 4:
            return
        self.graph.add_edge(start.get_position(), end.get_position())
        self.check_grid_power()

    def draw(self, screen: pygame.Surface):
        self.__draw_nodes(screen)
        self.__draw_connections(screen)
    
    def remove_node_at(self, pos: tuple[int,int]):
        node = self.nodes.get(pos, None)
        if node is not None and node.is_destructible():
            self.nodes.pop(pos, None)
            self.graph.remove_vertex(pos)
            self.total_poles += 1
    
    def get_node_at(self,pos: tuple[int,int]):
        return self.nodes.get(pos,None)

    def check_grid_power(self):
        house_power = self.drain_houses.copy()
        visited = set()
        for power_house in self.power_houses:
            power_house_power = power_house.get_power()
            node_queue = [(power_house,0)]
            while len(node_queue) > 0 and power_house_power > 0:
                (current_node, level) = node_queue.pop(-1)
                for node_pos in self.graph.get_vertex(current_node.get_position()):
                    next_node = self.nodes[node_pos]
                    if next_node in visited:
                        continue
                    if next_node not in house_power:
                        visited.add(current_node)
                        node_queue.append((next_node, level+1))
                        continue
                    if power_house_power > next_node.get_power() + level:
                        power_house_power += next_node.get_power() - level
                        house_power.remove(next_node)
                        
        if len(house_power) == 0:
            self.has_won = True
 
    def win_condition_met(self):
        return self.has_won

    @staticmethod
    def get_length(node1, node2):
        return ((node1[0] - node2[0])**2 + (node1[1] - node2[1])**2)**0.5

    def __draw_nodes(self, screen):
        for pole in self.nodes.values():
            pole.draw(screen)

    def __draw_connections(self, screen):
        for coords, neighbors in self.graph.get_vertices():
            for neighbor in neighbors:
                self.__draw_connection(screen, coords, neighbor)

    def __draw_connection(self, screen, coords, neighbor):
        pygame.draw.line(screen, self.__color, coords, neighbor)

    def __draw_connection(self, screen: pygame.Surface,startPos: tuple[int, int], endPos: tuple[int,int]):
        pygame.draw.line(screen, (0, 0, 0), index_to_coordinates(screen,*startPos), index_to_coordinates(screen, *endPos), 2)
