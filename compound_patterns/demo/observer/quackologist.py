from observer.observer import Observer

class Quackologist(Observer):
    def __init__(self)-> None:
        pass

    def update(self, duck)-> None:
        print("Quackologist: " + str(duck) + " just quacked.")
