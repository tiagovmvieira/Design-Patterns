from termcolor import colored
from home_theater_facade import *

if __name__ == '__main__':
    print(colored('------------------ FACADE PATTERN -------------------', 'white'))
    print(colored('------------------- HOME THEATER --------------------', 'blue'))
    home_theater_facade = HomeTheaterFacade()

    print(colored('\n------------------- MOVIE WATCH ---------------------', 'green'))
    home_theater_facade.watch_movie('Raiders of the Lost Ark')

    print(colored('\n-------------------- END MOVIE ----------------------', 'yellow'))
    home_theater_facade.end_movie()
