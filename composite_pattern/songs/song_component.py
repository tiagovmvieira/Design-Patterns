from __future__ import annotations
from abc import ABC, abstractmethod

class SongComponent(ABC):
    @abstractmethod
    def __init__(self):
        if self.__class__ == SongComponent:
            raise TypeError("Instantiating the Abstract Class")

    @property
    @abstractmethod
    def add(self)-> None:
        raise NotImplementedError

    @property
    @abstractmethod
    def remove(self, song_component: SongComponent)-> None:
        raise NotImplementedError

    @property
    @abstractmethod
    def get_group_name(self)-> str:
        raise NotImplementedError

    @property
    @abstractmethod
    def get_group_description(self)-> str:
        raise NotImplementedError

    @property
    @abstractmethod
    def get_component_index(self)-> int:
        raise NotImplementedError

    @property
    @abstractmethod
    def get_song_name(self)-> str:
        raise NotImplementedError

    @property
    @abstractmethod
    def get_band_name(self)-> str:
        raise NotImplementedError

    @property
    @abstractmethod
    def get_release_year(self)-> int:
        raise NotImplementedError

    def display_song_info(self)-> None:
        pass
