class Employee:
    """Common base class for all employees"""
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    @staticmethod
    def display_count():
        print("Total Employees: {0}".format(Employee.empCount))

    def display_employee(self):
        print("Name {name:12}   Salary {salary:12}".format(name=self.name, salary=self.salary))


emp1 = Employee("Zara", 12000)
emp2 = Employee("Manii", 9600)

emp1.age = 30

emp1.display_count()
emp2.display_count()
emp1.display_employee()
emp2.display_employee()

print("getattr", getattr(emp1, 'age'))
print("getattr", getattr(emp2, 'salary'))

print("Employee.__doc__:", Employee.__doc__)
print("Employee.__name__:", Employee.__name__)
print("Employee.__module__:", Employee.__module__)
print("Employee.__bases__:", Employee.__bases__)
print("Employee.__dict__:", Employee.__dict__)

