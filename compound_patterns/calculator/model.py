from typing import Union

class Model:
    def __init__(self):
        self.value = ''

    def calculate(self, caption: Union[str, int])-> str:
        if caption == 'C':
            self.value = ''
        elif isinstance(caption, int):
            self.value += str(caption)

        return self.value