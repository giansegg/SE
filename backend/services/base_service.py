from abc import ABC, abstractmethod

class CoordsService(ABC):
    @abstractmethod
    def get_coords(self, city, country):
        pass
