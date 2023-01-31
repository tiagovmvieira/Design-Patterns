from .chain import Chain
from .numbers import Numbers

class SubtractNumbers(Chain):
    def __init__(self)-> None:
        pass

    def set_next_chain(self, next_chain: Chain) -> None:
        self.next_chain = next_chain

    def calculate(self, request: Numbers)-> None:
        if request.get_calculation_wanted() == 'sub':
            print(f"{request.get_number_1()} + {request.get_number_2()} = {request.get_number_1() - request.number_2()}")
        else:
            self.next_chain.calculate(request)