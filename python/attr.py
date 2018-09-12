
class Cup(object):
    def __init__(self, name):
        self.name = name
        self.price = 0

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
    print(hasattr(cup2, 'new_name'))

    print('done')
