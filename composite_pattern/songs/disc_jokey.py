from song_group import SongGroup
from song_component import SongComponent
from song import Song

from termcolor import colored

if __name__ == '__main__':
    print(colored('------------------ COMPOSITE PATTERN ----------------', 'white'))
    industrial_music: SongComponent = SongGroup("Industrial", "is a style of experimental music that draws on transgressive and \
        provocative themes")

    heavy_metal_music: SongComponent = SongGroup("\nHeavy Metal", "is a genre of rock that developed in the late 1960s, largely \
        in the UK and in the US")
    
    dubstep_music: SongComponent = SongGroup("\nDubstep", "is a genre of eletronic dance music that originated in South London \
        England")

    every_song: SongComponent = SongGroup("Song List", "Every Song Available")
    every_song.add(industrial_music)

    industrial_music.add(Song("Head Like a Hole", "NIN", 1990))
    industrial_music.add(Song("Headhunter", "Front 242", 1988))

    industrial_music.add(dubstep_music)

    dubstep_music.add(Song("Centipede", "Knife Party", 2012))
    dubstep_music.add(Song("Tetris", "Doctor P", 2011))

    every_song.add(heavy_metal_music)

    heavy_metal_music.add(Song("War Pigs", "Black Sabath", 1970))
    heavy_metal_music.add(Song("Ace of Spades", "Motorhead", 1980))

    every_song.display_song_info()