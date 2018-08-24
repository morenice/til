if __name__ == '__main__':
    a = [1,2,3]
    b = a
    c = [1,2,3]

    if a == b:
        print('a == b')

    if a is b:
        print('a is b')

    if a == c:
        print('a == c')

    if a is c:
        print('a is c')
