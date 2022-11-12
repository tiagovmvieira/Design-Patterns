import inspect

from streaming_player import StreamingPlayer

class Amplifier:
    def __init__(self):
        self.no_speakers = 5
        self.no_subwoofers = 1

    def on(self):
        print(f"{self.__class__.__name__} {inspect.stack()[0][3]}")

    def off(self):
        print(f"{self.__class__.__name__} {inspect.stack()[0][3]}")

    def set_streaming_player(self, player: StreamingPlayer):
        self.player = player
        print(f"{self.__class__.__name__} setting streaming player to {self.player.__class__.__name__}")

    def set_surround_sound(self):
        print(f"{self.__class__.__name__} sound on ({self.no_speakers} speaker(s), {self.no_subwoofers} subwoofer(s)")

    def set_volume(self, volume: int):
        print(f"{self.__class__.__name__} setting volume to {volume}")