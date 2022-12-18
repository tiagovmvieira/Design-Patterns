from abc import ABC, abstractmethod

class ControllerInterface(ABC):
    @abstractmethod
    def start(self)-> None:
        pass

    @abstractmethod
    def stop(self)-> None:
        pass

    @abstractmethod
    def increase_bpm(self)-> None:
        pass

    @abstractmethod
    def decrease_bpm(self)-> None:
        pass

    @abstractmethod
    def set_bpm(self, bpm: int)-> None:
        pass