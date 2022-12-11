from abc import ABC, abstractmethod

class SongComponent(ABC):
    @abstractmethod
    def __init__(self):
        if self.__class__ == SongComponent:
            raise TypeError("Instantiating the Abstract Class")

    def add(self):
        from song import Song #avoid circular imports
        if self.__class__ == Song:
            raise AttributeError("This method should not be implemented on a Song class")

    def remove(self):
        from song import Song #avoid circular imports
        if self.__class__ == Song:
            raise AttributeError("This method should not be implemented on a Song class")

    def get_song_name(self)-> str:
        from song_group import SongGroup #avoid circular imports
        if self.__class__ == SongGroup:
            raise AttributeError("This method should not be implemented on a SongGroup class")

    def get_band_name(self)-> str:
        from song_group import SongGroup #avoid circular imports
        if self.__class__ == SongGroup:
            raise AttributeError("This method should not be implemented on a SongGroup class")

    def get_release_year(self)-> str:
        from song_group import SongGroup #avoid circular imports
        if self.__class__ == SongGroup:
            raise AttributeError("This method should not be implemented on a SongGroup class")

    @abstractmethod
    def display_song_info(self)-> None:
        if self.__class__ == SongComponent:
            raise AttributeError("This method should not be implemented on a SongComponent class")
