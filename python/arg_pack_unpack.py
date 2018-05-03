def test_function(*args, **kwargs):
    # *args is tuple
    # **kwargs is key-value dict
    print(args)
    print(kwargs)


if __name__ == "__main__":

    # *args
    print('test_function(1,2,3)')
    test_function(1,2,3)

    # **kwargs case1
    print('test_function(a=1, b=2)')
    test_function(a=1, b=2)

    # **kwargs case2
    dic = dict()
    dic['a'] = 1
    dic['b'] = 2

    print('test_function(dic)')
    test_function(dic)

    print('test_function(**dic)')
    test_function(**dic)

    a = [1, 2, 3]
    print('test_function(*list)')
    test_function(*a)
    print('test_function(list)')
    test_function(a)
