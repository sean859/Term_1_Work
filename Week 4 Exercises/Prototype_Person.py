from abc import ABC, abstractmethod

# Prototype
class Person(ABC):
    def __init__(self, name: str):
        self.name = name
        
    @abstractmethod
    def clone(self):
        pass
    
    @abstractmethod
    def display(self):
        pass

    def get_name(self):
        return self.name
    
    def set_name(self, name: str):
        self.name = name
