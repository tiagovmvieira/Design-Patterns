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
            value = float(self.value) if '.' in self.value else int(self.value)

            self.value = str(value / 100)
        elif caption == '.':
            if not caption in self.value:
                self.value += caption
        elif caption == '=':
            value = self._evaluate()

            if '.0' in str(value):
                value = int(value)
            
            self.value = str(value)
        elif isinstance(caption, int):
            self.value += str(caption)
        else:
            if self.value:
                self.operator = caption
                self.previous_value = self.value
                self.value = ''

        return self.value

    def _evaluate(self)->Union[int, float]:
        return eval(self.previous_value + self.operator + self.value)