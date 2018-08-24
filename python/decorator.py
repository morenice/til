class SampleDeco:
    def __init__(self, f):
        self.func = f

    def __call__(self, *args, **kwargs):
        print("called prepare decorate function")
        self.func(*args, **kwargs)
        print("called after decorate function")


@SampleDeco
def my_function(name):
    print("Hello, %s" % name )

if __name__ == "__main__":
    my_function("morenice")
