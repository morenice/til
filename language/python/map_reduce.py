# lambda: anonymous function
#
def f1(i):
    return i*i

l1 = lambda x: x*x

print(f1(10))
print(l1(10))


def f2(i):
    if i > 0:
        return (i*10)+5
    return -1

l2 = lambda i: (i*10)+5 if i > 0 else -1

print(f2(10))
print(l2(10))


# map: sequence data to function mapping
#
list1 = list(map(lambda x:x*2, [i for i in range(1,10)]))
print(list1)


# reduce
#
from functools import reduce

result = reduce(lambda x,y:x+y, [i for i in range(1,10)])
print(result)
