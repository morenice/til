import functools


# Case 1
#
def reverse_numeric(x, y):
    return x - y

print('sort by functools.cmp_to_key ...')
print(sorted([5, 2, 4, 1, 3], key=functools.cmp_to_key(reverse_numeric)))
print('')


# Case 2
#
sample_data = [
    {
        'name': 'aaa',
        'age': 12,
        'score': {
            'math': 90
        }
    },
    {
        'name': 'bbb',
        'age': 15,
        'score': {
            'math': 20
        }
    },
    {
        'name': 'ccc',
        'age': 18,
        'score': {
            'math': 95
        }
    }
]

print('sort by math desc')
print(sorted(sample_data, key=lambda data: data['score']['math'], reverse=True))
print('')

print('sort by age asc')
print(sorted(sample_data, key=lambda data: data['age']))
print('')

