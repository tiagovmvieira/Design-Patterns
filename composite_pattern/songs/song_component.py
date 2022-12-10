from abc import ABC, abstractmethod

class SongComponent(ABC):
    @abstractmethod
    def __init__(self):
        if self.__class__ == SongComponent:
            raise TypeError("Instantiating the Abstract Class")

    def add(self):
        if self.__class__ == SongComponent:
            raise AttributeError("This method should not be implemented on a SongComponent class")

    def remove(self):
        if self.__class__ == SongComponent:
            raise AttributeError("This method should not be implemented on a SongComponent class")

    def get_song_name(self)-> str:
        if self.__class__ == SongComponent:
            raise AttributeError("This method should not be implemented on a SongComponent class")

    def get_band_name(self)-> str:
        if self.__class__ == SongComponent:
            raise AttributeError("This method should not be implemented on a SongComponent class")

    def get_release_year(self)-> str:
        if self.__class__ == SongComponent:
            raise AttributeError("This method should not be implemented on a SongComponent class")

    @abstractmethod
    def display_song_info(self)-> None:
        if self.__class__ == SongComponent:
            raise AttributeError("This method should not be implemented on a SongComponent class")
