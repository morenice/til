def singleton(cls):
    instances = {}

    def wrap(*arg, **argv):
        if cls not in instances:
            instances[cls] = cls(*arg, **argv)
        return instances[cls]

    return wrap


@singleton
class ClassA:
    a = 10
    b = 5

    def __init__(self, a=1, b=2):
        self.a = a
        self.b = b

class ClassB:
    c = 10
    d = 5


print(ClassA(a=4, b=5).a)
print(ClassA().b)
print(ClassB().c)
