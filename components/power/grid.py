import pygame

from components.power.endpoint import PowerEndpoint
from components.power.node import PowerNode, BlockNode
from components.power.pole import PowerPole
from data_structures.undirected_graph import UndirectedGraph
from utils import index_to_coordinates


class PowerGrid:
    def __init__(self,total_poles = 10):
        self.graph = UndirectedGraph()
        self.nodes: dict[tuple[int, int], PowerNode] = {} 
        self.total_poles = total_poles
        self.max_poles = total_poles
        self.power_houses = []
        self.drain_houses = []
        self.has_won = False

    def get_towers_used(self):
        return (self.max_poles, self.total_poles)

    def add_power_node(self, power_node: PowerNode):
        if power_node.get_position() not in self.nodes and self.total_poles > 0: 
            self.nodes[power_node.get_position()] = power_node 
            self.graph.add_vertex(power_node.get_position()) 

            if not isinstance(power_node, PowerEndpoint):
                if isinstance(power_node, PowerPole):
                    self.total_poles -= 1
                return
            
            if power_node.get_power() > 0:
                self.power_houses.append(power_node)
            else:
                self.drain_houses.append(power_node)

    def add_connection(self, start: PowerNode, end: PowerNode):
        if PowerGrid.get_length(start.get_position(), end.get_position()) > 4:
            return False
        if self.__connection_check(start, end):
            return False
        if isinstance(start, BlockNode) or isinstance(end, BlockNode):
            return False
        self.graph.add_edge(start.get_position(), end.get_position())
        self.check_grid_power()
        return True

    def __connection_check(self, start: PowerNode, end: PowerNode):
        if not start.is_conductive() and not end.is_conductive():
            return True
        if not  start.is_conductive() and self.__nr_connections(start) > 0:
            return True
        if not end.is_conductive() and self.__nr_connections(end) > 0:
            return True
        if self.__check_for_obstruction(start, end):
            return True
        return False 

    def __check_for_obstruction(self,start: PowerNode, end: PowerNode):
        for point in self.__get_line(start.get_position(), end.get_position()):
            if point in self.nodes and not point == start.get_position() and not point == end.get_position():
                return True
        return False
    
    @staticmethod
    def __get_line(start:tuple[int,int], end:tuple[int,int]):
        """Return a list of coordinates between start and end."""
        x0, y0 = start
        x1, y1 = end
        dx = abs(x1 - x0)
        dy = abs(y1 - y0)
        sx = 1 if x0 < x1 else -1
        sy = 1 if y0 < y1 else -1
        err = dx - dy
        line = []
        while True:
            line.append((x0, y0))
            if x0 == x1 and y0 == y1:
                break
            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x0 += sx
            if e2 < dx:
                err += dx
                y0 += sy
        return line

    def __nr_connections(self, node: PowerNode):
        return len(self.graph.get_vertex(node.get_position()))

    def draw(self, screen: pygame.Surface):
        self.__draw_nodes(screen)
        self.__draw_connections(screen)
    
    def remove_node_at(self, pos: tuple[int,int]):
        node = self.nodes.get(pos, None)
        if node is None or isinstance(node, BlockNode):
            return False
        self.graph.remove_vertex(pos)
        if node.is_destructible():
            self.nodes.pop(pos, None)
            self.total_poles += 1
            self.check_grid_power()
            return True
        self.graph.add_vertex(pos)
        self.check_grid_power()
        return True
                      
    def resize(self, screen: pygame.Surface):
        for node in self.nodes.values():
            node.resize(screen)

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
                if power_house_power - level < 3:
                    break
                for node_pos in self.graph.get_vertex(current_node.get_position()):
                    next_node = self.nodes[node_pos]
                    if next_node in visited:
                        continue
                    if isinstance(next_node,PowerPole):
                        next_node.set_power(1 + level)
                    if next_node not in house_power:
                        visited.add(current_node)
                        node_queue.append((next_node, level+1))
                        continue
                    if power_house_power > next_node.get_power() + level:
                        power_house_power += next_node.get_power() - level
                        house_power.remove(next_node)
            power_house.set_remaining_power(power_house_power) 
                        
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
