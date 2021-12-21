from abc import ABC, abstractmethod


class Car(ABC):

    @abstractmethod
    def __init__(self, model, speed_limit):
        self.model = model
        self.speed_limit = speed_limit
        self.is_taken = False

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if len(value) < 4:
            raise ValueError(f"Model {self.model} is less than 4 symbols!")
        self.__model = value

    @property
    @abstractmethod
    def speed_limit(self):
        pass

    @speed_limit.setter
    @abstractmethod
    def speed_limit(self, value):
        pass
