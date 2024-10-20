class Person:
    def __init__(self, name, age):
        self.__name = name
        self.age = age

    def greating(self):
        print(f"Hello {self.__name}")
        Person.__getPerson()

    @staticmethod
    def __getPerson():
        print(f"Person name ")


person = Person("Ravi", 30)
person.greating()
print(person.age)

