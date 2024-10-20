class Employee(object):
    def __int__(self, name, city):
        self.name=  name
        self.city = city

    def get_employee(name, city):
        print(f"name: {name} city: {city}")

    def __str__(self):
        Employee.get_employee(self.name, self.city)


obj = Employee()
