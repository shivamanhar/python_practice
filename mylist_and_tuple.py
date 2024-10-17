import random
types = (('a', 2),('b', 3), ('c', 4))
new_types = random.choices(*list(zip(*types)))[0]
#print(new_types)

nums_squared_gc = (num**2 for num in range(5))

#print(type(nums_squared_gc))

#print(next(nums_squared_gc))
#print(next(nums_squared_gc))
#print(next(nums_squared_gc))
#print(next(nums_squared_gc))


def create_list(n=5):
    for i in range(n):
        yield i

for i in create_list(5):
    print(i)


rec_N = random.choices([2, 3, 4, 7], weights = [1, 2, 4, 9],k= 1)[0]
print(f"rec_N {rec_N}")


n = [i for i in range(1, 10)]
print(n)
n[2]  *= 5
print(n[2])

