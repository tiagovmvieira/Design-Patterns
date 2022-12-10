from id_department import IDepartment

class Development(IDepartment):
    def __init__(self, no_employees)-> None:
        super().__init__(no_employees)

    def print_department(self)-> None:
        print(f"Development Department - Number of employees: {self.no_employees}")