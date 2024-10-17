names = ['David Beazley', 'Brian Jones','Raymond Hettinger', 'Ned Batchelder']

def name_split(names):
    for name in names:
        print(name.split()[-1])

name_split(names)


sorted_name = sorted(names, key = lambda  name: name.split()[-1].lower())
print(sorted_name)
