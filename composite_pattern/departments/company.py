from accounting_department import Accounting
from development_department import Development
from parent_department import ParentDeparment

from termcolor import colored

if __name__ == '__main__':
    print(colored('------------------ COMPOSITE PATTERN ----------------', 'white'))
    accounting_department = Accounting(200)
    development_department = Development(170)

    administration_department = ParentDeparment(30)
    administration_department.add(accounting_department)
    administration_department.add(development_department)

    administration_department.print_department()
