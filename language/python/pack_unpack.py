def test_arg(*args, **kwargs):
    # *args is tuple
    # **kwargs is key-value dict
    print(f'args: {args}')
    print(f'kwargs: {kwargs}', end='\n\n')


def arg_pack_function():
    # *args
    print('test_arg(1,2,3)')
    test_arg(1,2,3)

    # **kwargs case1
    print('test_arg(a=1, b=2)')
    test_arg(a=1, b=2)

    # **kwargs case2
    dic = dict()
    dic['a'] = 1
    dic['b'] = 2

    print('test_arg(dic)')
    test_arg(dic)

    print('test_arg(**dic)')
    test_arg(**dic)

    a = [1, 2, 3]
    print('test_arg(*list)')
    test_arg(*a)
    print('test_arg(list)')
    test_arg(a)


def pack_unpack1():
    print('pack and unpack...')
    print('a = [1,2,3]')
    print('b = [2,4,5]')
    a = [1,2,3]
    b = [2,4,5]

    # merge a, b
    c = (*a, *b)
    d = {*a,*b}
    print(f'c = {c}')
    print(f'd = {d}')


if __name__ == "__main__":
    arg_pack_function()
    pack_unpack1()
