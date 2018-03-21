class Employee:
    """Common base class for all employees"""
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employees: {0}".format(Employee.empCount))

    def displayEmployee(self):
        print("Name {name:12}   Salary {salary:12}".format(name = self.name, salary = self.salary))

emp1 = Employee("Zara", 12000)
emp2 = Employee("Manii", 9600)

emp1.displayCount()
emp2.displayCount()
emp1.displayEmployee()
emp2.displayEmployee()


