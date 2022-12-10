from id_department import IDepartment

class Accounting(IDepartment):
    def __init__(self, no_employees)-> None:
        super().__init__(no_employees)

    def print_department(self)-> None:
        print(f"Accounting Department - Number of employees: {self.no_employees}")