def sample(i):
    return i ** 2


def decorate_function(func):
    prefix = '[PREFIX] '
    def loggigg():
        print('{} Start {}'.format(prefix, func.__name__))

        # Closures
        #  - scoped name binding in languguage with first-class.
        #  - free variable of the function.
        #   (variables that are used locally, but defined in an enclosing scope)
        func()
        print('{} End {}'.format(prefix, func.__name__))
    return loggigg


@decorate_function
def hello_world():
    print('hello world')


class SampleDecorator:
    def __init__(self, f):
        self.func = f

    def __call__(self, *args, **kwargs):
        print("called prepare decorate function")
        self.func(*args, **kwargs)
        print("called after decorate function")


@SampleDecorator
def my_function(name):
    print("Hello, %s" % name )


if __name__ == "__main__":
    # Functions are first-class citizens in Python
    # 1. possible that assign in array
    # 2. possible as argument
    #
    print('first-class example')
    funcs = [sample]
    print(funcs[0])
    print(funcs[0](3))
    print('')

    # example for function decorator
    #
    print('logging fucntion decorator')
    hello_world()
    print(dir(hello_world))
    print(hello_world.__closure__)

    # closure cell
    print(dir(hello_world.__closure__[0]))
    print(hello_world.__closure__[0].cell_contents)
    print('')

    # possible that assign static variable to function
    hello_world.static_var = 4
    print(hello_world.static_var)
    print(dir(hello_world))
    print('')

    # example for class decorator
    #  - possible wrapper and customize
    #
    print('logging class decorator')
    my_function("morenice")
    print(dir(my_function))
    print('')
