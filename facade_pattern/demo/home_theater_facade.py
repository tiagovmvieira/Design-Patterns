from theater_lights import TheaterLights
from streaming_player import StreamingPlayer
from amplifier import Amplifier
from projector import Projector
from screen import Screen
from popcorn_popper import PopcornPopper

class HomeTheaterFacade:
    def __init__(self, amplifier: Amplifier = Amplifier(), player: StreamingPlayer = StreamingPlayer(), projector: Projector = Projector(),\
                screen: Screen = Screen(), lights: TheaterLights = TheaterLights(), popcorn_popper: PopcornPopper = PopcornPopper())-> None:
        self.amplifier = amplifier
        self.player = player
        self.projector = projector
        self.screen = screen
        self.lights = lights
        self.popcorn_popper = popcorn_popper

    def watch_movie(self, movie_name: str):
        self.movie_name = movie_name
        print('Get ready to watch a movie...')
    
        self.popcorn_popper.on()
        self.popcorn_popper.pop()
        self.lights.dim(10)
        self.screen.down()
        self.projector.on()
        self.projector.wide_screen_mode()
        self.amplifier.on()
        self.amplifier.set_streaming_player(player=self.player)
        self.amplifier.set_surround_sound()
        self.amplifier.set_volume(5)
        self.player.on()
        self.player.play(movie_name=self.movie_name)

    def end_movie(self):
        print('Shutting movie theater down...')

        self.popcorn_popper.off()
        self.lights.on()
        self.screen.up()
        self.projector.off()
        self.amplifier.off()
        self.player.stop()
        self.player.off()

    def listen_to_radio(self):
        pass

    def end_radio(self):
        pass