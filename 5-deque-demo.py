from collections import deque
import collections

# Declaring deque 
queue = deque(['name','age', 'DOB'])

print(queue)


# Operation on deque
# append - Insert the value is its argument to the right end
# appendleft - Insert in left end
# pop - Delete in right end
# popleft - delete in left end

# Initializing deque

de = collections.deque([1, 2, 3])

# Insert 
de.append(4)

print(de)
de.appendleft(9)
print(de)