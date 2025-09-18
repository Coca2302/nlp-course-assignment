from abc import ABC, abstractmethod

class Tokenize(ABC):    
    @abstractmethod
    def tokenize(self, text: str):
        pass