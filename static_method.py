class MethodOperation(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def get_name():
        print(f"Hello")

    @staticmethod
    def call_get_name():
        MethodOperation.get_name()

MethodOperation.get_name()
MethodOperation.call_get_name()

