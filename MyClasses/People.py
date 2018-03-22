class Parent:  # define parent class
    parentAttr = 100

    def __init__(self):
        print("Calling parent constructor")

    @staticmethod
    def parentMethod():
        print('Calling parent method')

    @staticmethod
    def setAttr(attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print("Parent attribute :", Parent.parentAttr)


class Child(Parent):  # define child class
    def __init__(self):
        super().__init__()
        print("Calling child constructor")

    def childMethod(self):
        print('Calling child method')
