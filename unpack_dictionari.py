from pprint import pprint 
# Function with keyword arguments
def introduce(name, age, city):
    print(f"My name is {name}, I'm {age} years old, and I live in {city}.")

# Dictionary of arguments
person_info = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
pprint(person_info)

# Using ** to unpack dictionary
introduce(**person_info)


name = "shiva"

def getChar(a,b,c,d,e):
    print(f"a={a}, b={b}, c= {c}, d={d}, e= {e}")

getChar(*name)

def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4))


def avg(first, *all_other):
    other_number = all_other
    print(other_number)
    print(f"types {type(other_number)}")


avg(4, 7, 9, 10)

def make_element(**keyarg):
    print(type(keyarg))


student_detail = {'name':'Goviend','age':30}

make_element(**student_detail)

hari = student_detail.get("hari", "patwari")
print(hari)
