from abc import ABC, abstractmethod

class BeatModelInterface(ABC):
    @abstractmethod
    def initialize(self)-> None:
        pass

    @abstractmethod
    def on(self)-> None:
        pass

    @abstractmethod
    def off(self)-> None:
        pass

    @abstractmethod
    def set_bpm(bpm: int)-> None:
        pass

    @abstractmethod
    def get_bpm(self)-> int:
        pass

    @abstractmethod
    def register_observer(self, observer)-> None:
        pass

    @abstractmethod
    def remove_observer(self, observer)-> None:
        pass

    @abstractmethod
    def register_observer(self, observer)-> None:
        pass

    @abstractmethod
    def remove_observer(self, observer)-> None:
        pass
