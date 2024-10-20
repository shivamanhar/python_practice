class MyClass(object):
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}!")

# Creating an instance of MyClass
obj = MyClass("Alice")
#obj.greet()  # Output: Hello, Alice!
