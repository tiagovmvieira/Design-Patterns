from id_department import IDepartment
from typing import List

class ParentDeparment(IDepartment):
    def __init__(self, no_employees)-> None:
        super().__init__(no_employees)
        self.base_employees = no_employees
        self.sub_departments : List[IDepartment] = []

    def add(self, department: IDepartment)-> None:
        self.sub_departments.append(department)
        self.no_employees += department.no_employees

    def print_department(self)-> None:
        print("Parent Deparment")
        print(f"Parent Department - Base employees: {self.base_employees}")

        for department in self.sub_departments:
            department.print_department()

        print(f"Total number of employees: {self.no_employees}")