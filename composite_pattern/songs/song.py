from song_component import SongComponent

class Song(SongComponent):
    get_song_name, get_band_name, get_release_year = 'yes', 'yes', 'yes'
    add, remove, get_group_name, get_group_description, get_component_index = 'no', 'no', 'no', 'no', 'no'

    def __init__(self, song_name: str, band_name: str, release_year: int):
        super().__init__()
        self.song_name = song_name
        self.band_name = band_name
        self.release_year = release_year

    def get_song_name(self)-> str:
        return self.song_name

    def get_band_name(self)-> str:
        return self.band_name

    def get_release_year(self)-> int:
        return self.release_year

    def display_song_info(self)-> None:
        print(self.get_song_name() + " was recorded by " + self.get_band_name() + " in " + str(self.get_release_year()))