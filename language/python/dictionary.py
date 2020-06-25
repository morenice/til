if __name__ == "__main__":
    # Create dictionary with three entries.
    values = {'a': 1, 'b': 2, 'c': 3}

    # raise exception
    try:
        print(values['d'])
    except KeyError as e:
        print(f'Error: {e}')

    # avoid KeyError exception
    # return None
    print(values.get('d'))

    # get 'a'
    print(values.get('a'))

    # not using exception technic
    values2 = {'a': [], 'b': [1,2,3]}
    for i in values2.get('c', []):
        print(i)

    # comprehension
    new_value = {i: str(i) for i in values2.get('b', [])}
    print(new_value)

