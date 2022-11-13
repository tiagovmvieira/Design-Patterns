import inspect

class StreamingPlayer:
    def __init__(self):
        pass

    def on(self):
        print(f"{self.__class__.__name__} {inspect.stack()[0][3]}")

    def off(self):
        print(f"{self.__class__.__name__} {inspect.stack()[0][3]}")

    def play(self, movie_name: str):
        self.movie_name = movie_name
        print(f"{self.__class__.__name__} playing {movie_name}")

    def stop(self):
        print(f"{self.__class__.__name__} stopped {self.movie_name}")