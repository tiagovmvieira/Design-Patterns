from typing import Union

class Model:
    def __init__(self):
        self.previous_value: str = ''
        self.value: str = ''
        self.operator: str = ''

    def calculate(self, caption: Union[str, int])-> str:
        if caption == 'C':
            self.previous_value = ''
            self.value = ''
            self.operator = ''
        elif caption == '+/-':
            self.value = str(int(self.value) * -1)
        elif caption == '%':
            self.value = str(int(self.value) / 100)
        elif caption == '.':
            if not caption in self.value:
                self.value += caption
        elif caption == '=':
            self.value = str(self._evaluate())

        elif isinstance(caption, int):
            self.value += str(caption)
        else:
            if self.value:
                if caption == '/' and isinstance(self.value, int):
                    self.operator = caption
                    self.previous_value = self.value
                self.value = ''

        return self.value

    def _evaluate(self)-> float:
        return eval(self.previous_value + self.operator + self.value)