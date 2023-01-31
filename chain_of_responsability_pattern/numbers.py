class Numbers:
    def __init__(self, number_1: int, number_2: int, calculation_wanted: str)-> None:
        self.number_1 = number_1
        self.number_2 = number_2
        self.calculation_wanted = calculation_wanted

    def get_number_1(self)-> int:
        return self.number_1

    def get_number_2(self)-> int:
        return self.number_2

    def get_calculation_wanted(self)-> int:
        return self.calculation_wanted