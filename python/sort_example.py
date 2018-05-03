import functools

def reverse_numeric(x, y):
    return x - y

print(sorted([5, 2, 4, 1, 3], key=functools.cmp_to_key(reverse_numeric)))
