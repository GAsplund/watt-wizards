from abc import abstractmethod

from components.power.node import PowerNode


class PowerEndpoint(PowerNode):
    @abstractmethod
    def get_power(self):
        pass
