class Cup(object):
    def __init__(self, name):
        self.name = name
        self.price = 0


class MyClass:
    pass


def myfunc():
    pass


if __name__ == '__main__':
    cup1 = Cup('aaa')
    cup2 = Cup('bbb')

    # get attribute of object
    print(getattr(cup1, 'name'))
    print(getattr(cup2, 'name'))

    try:
        name = getattr(cup1, 'country')
    except Exception as e:
        print('occured getattr except:' + str(e))

    # check attribute
    print(hasattr(cup2, 'new_name'))
    print(getattr(cup2, 'new_name', 'default'))

    # set attribute
    setattr(cup2, 'new_name', 'default')
    print(hasattr(cup2, 'new_name'), end='\n\n')

    # access class attribute
    obj = MyClass()
    print(obj.__class__.__name__)
    print(myfunc.__name__)

