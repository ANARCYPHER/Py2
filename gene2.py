import itertools

squares = (x**2 for x in itertools.count(1))

print(type(squares))
