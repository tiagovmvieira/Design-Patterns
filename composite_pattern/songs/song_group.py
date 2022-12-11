from song_component import SongComponent

from typing import List
from collections.abc import Iterator, Iterable

class SongGroupIterator(Iterator):
    def __init__(self, song_components: List[SongComponent])-> None:
        self.song_components = song_components
        self.position = 0

    def __next__(self)-> SongComponent:
        try:
            song_component = self.song_components[self.position]
            self.position += 1
        except IndexError:
            raise StopIteration()

        return song_component

class SongGroup(SongComponent, Iterable):
    def __init__(self, group_name: str, group_description: str):
        super().__init__()
        self.song_components: List[SongComponent] = []
        self.group_name = group_name
        self.group_description = group_description

    def __iter__(self)-> SongGroupIterator:
        return SongGroupIterator(self.song_components)

    def get_group_name(self)-> str:
        return self.group_name

    def get_group_description(self)-> str:
        return self.group_description

    def add(self, song_component: SongComponent):
        self.song_components.append(song_component)

    def remove(self, song_component: SongComponent):
        self.song_components.remove(song_component)

    def get_component_index(self, song_component_index: int)-> SongComponent:
        return self.song_components[song_component_index]

    def display_song_info(self)-> None:
        print(self.get_group_name() + " " + self.get_group_description() + "\n")

        for song_component in self.song_components:
            song_component.display_song_info()