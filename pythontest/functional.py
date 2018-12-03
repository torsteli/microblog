a = [1,2,3,5,7,9]
b = [2,3,5,6,7,8]

print(a)
print(b)
print(list(filter(lambda x: x in a, b)))  # prints out [2, 3, 5, 7]

from operator import add
print(map(add, a,b))