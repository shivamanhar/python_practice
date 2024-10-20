class A:
    def show(self):
        print("Welcome")

class B:
    def show(self):
        obj = A()
        obj.show()


obj = B()
obj.show()
