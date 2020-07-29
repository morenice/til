from collections import namedtuple


if __name__ == "__main__":
    """
    tuple: immutable list
    """
    t1 = (1,2,3,4,5)
    t2 = 1,
    t3 = (1,'a', 4.0, 5, 'b', )

    print(f't1: {t1}')
    print(f't2: {t2}')
    print(f't3: {t3}')

    # possible key of dict
    d1 = dict()
    d1[t1] = 'immutble key'

    # Named tuple
    #
    Car = namedtuple('Car', 'name count')

    car1 = Car('lacetti', 1)
    car2 = Car('sonata', 10)
    print(f'{type(car1)}: {car1}')
    print(f'{type(car2)}: {car2}')

    is_tuple = True if issubclass(Car, tuple) else False
    print(is_tuple)
    print(car1.name)

