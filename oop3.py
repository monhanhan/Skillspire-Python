class Person:
    def __init__(self, name, idNum):
        self.name = name
        self.idNum = idNum

    def display(self):
        print("Name:", self.name, "\nID Number:", self.idNum)


class Employee(Person):
    def __init__(self, name, idNum, salary, title):
        super().__init__(name, idNum)
        self.salary = salary
        self.title = title

    def display(self):
        Person.display(self)
        print("Salary:", self.salary, "\nTitle:", self.title)


def main():
    person = Person("Karl", 1)
    employee = Employee("Chris", 2, 5, "King of all Cosmos")

    print()
    person.display()
    print()
    employee.display()
    print()


main()
