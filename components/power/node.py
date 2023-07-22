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
    

class BlockNode(PowerNode):
    def __init__(self,position: tuple[int, int] ):
        super().__init__(position)
    
    def is_conductive(self):
        return False

    def is_destructible(self):
        return False
