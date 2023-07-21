from abc import ABC, abstractmethod


class PowerNode(ABC):
    def __init__(self, position: tuple[int, int] ):
        self.position = position
    
    def get_position(self):
        return self.position
        
    @abstractmethod
    def is_conductive(self):
        pass
    @abstractmethod
    def is_destructible(self):
        pass