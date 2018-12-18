import json


def basic():
    len('aaaa')
    str(1)

    try:
        a = 'aaa' + 2
    except TypeError as e:
        print('Type Error: {0}'.format(e))


def dict_to_str():
    print('dict to str')
    d1 = {'a':1, 'b':'string'}
    d1_str = str(d1)
    print(d1_str)

    # This isn't secure because using eval function.
    d2 = eval(d1_str)
    if d1 == d2:
        print('eval function')

def dict_to_str2():
    print('dict to str 2')
    d1 = {'a':1, 'b':'string'}
    d1_str = json.dumps(d1)
    print(d1_str)

    d2 = json.loads(d1_str)
    if d1 == d2:
        print('json function')


def split():
    str1 = 'Thu,1,10,except'
    print('string split example: {0}'.format(str1))

    # ',' : seperator
    elements = str1.split(',')
    for el in elements:
        print(el)


def join():
    list1 = ['1', 'in', 'out']
    print('string join example: {0}'.format(':'.join(list1)))


def index():
    str1 = '--; select * from ...'
    print('string find and index example: {0}'.format(str1))

    # find function will  return index
    if str1.find('--;') >= 0:
        print('find it --;')

    # index: 3 to end
    print(str1[3:])

    # index: end 3 character
    print(str1[-3:])


def formating():
    # python3: format
    name = 'Roll'
    age = 20
    '{0}: {1}'.format(name, age)

    # python 3.6: f-string
    name2 = 'Kell'
    age2 = 40
    f'{name2}: {age2}'


if __name__ == '__main__':
    print('This is ' + 'string' + ' example')
    basic()
    dict_to_str()
    dict_to_str2()
    split()
    join()
    index()
    formating()

