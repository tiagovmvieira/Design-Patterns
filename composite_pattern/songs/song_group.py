from typing import List
from song_component import SongComponent

class SongGroup(SongComponent):
    def __init__(self, group_name: str, group_description: str):
        super().__init__()
        self.song_components: List[SongComponent] = []
        self.group_name = group_name
        self.group_description = group_description

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