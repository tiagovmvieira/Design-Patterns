from add_numbers import AddNumbers
from subtract_numbers import SubtractNumbers
from multiply_numbers import MultiplyNumbers
from divide_numbers import DivideNumbers
from numbers import Numbers

from termcolor import colored


class TestCalcChain:
    def __init__(self):
        chain_element_1 = AddNumbers()
        chain_element_2 = SubtractNumbers()
        chain_element_3 = MultiplyNumbers()
        chain_element_4 = DivideNumbers()

        chain_element_1.set_next_chain(chain_element_2)
        chain_element_2.set_next_chain(chain_element_3)
        chain_element_3.set_next_chain(chain_element_4)

        request = Numbers(1, 2, 'add')

        chain_element_1.calculate(request)


if __name__ == '__main__':
    print(colored('----------- CHAIN OF RESPONSABILITY PATTERN ---------', 'white'))
    test_calc_chain = TestCalcChain()

