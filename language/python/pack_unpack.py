def pack_function():
    def func1(*args, **kwargs):
        # *args is tuple
        # **kwargs is key-value dict
        print(f'args: {args}')
        print(f'kwargs: {kwargs}', end='\n\n')

    # *args
    print('func1(1,2,3)')
    func1(1,2,3)

    # **kwargs case1
    print('func1(a=1, b=2)')
    func1(a=1, b=2)

    # **kwargs case2
    dic = dict()
    dic['a'] = 1
    dic['b'] = 2

    print('func1(dic)')
    func1(dic)

    print('func1(**dic)')
    func1(**dic)

    a = [1, 2, 3]
    print('func1(*list)')
    func1(*a)
    print('func1(list)')
    func1(a)


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


def example_count_all_element():
    print('count all element ...')

    a = [1,2,3,4,5]
    b = [[1,2,3],[4,5,6],[7,8]]
    c = [[[1,2,3],[4,5,6],[7]],[4,5,6],[[1],[5,6,7]]]
    d = ['a', [1,'b',99], 'c']

    def count(*args):
        try:
            iter(args)
        except TypeError:
            return len(args)

        return sum([count(*arg) for arg in args])

    # a=>5, b=>8, c=>12, d=>5
    print(count(a))
    print(count(b))
    print(count(c))
    #print(count(d))


if __name__ == "__main__":
    pack_function()
    pack_unpack1()
    example_count_all_element()
