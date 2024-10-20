class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age}")


class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def say_hell(self):
        super().say_hello()
        print(f"I am a studen is grade  {self.grade}.")


person = Person("john", 30)
person.say_hello()

student = Student("mary", 18, 12)

student.say_hello()
