from abc import ABC, abstractmethod


class Document(ABC):

    def __init__(self, titre):
        self.titre = titre
        self.__disponible = True  


    @property
    def disponible(self):
        return self.__disponible

    def changeEtat (self, disponible):
        self.__disponible = disponible

    @abstractmethod
    def emprunter(self):
        pass

    @abstractmethod
    def retourner(self):
        pass
