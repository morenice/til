if __name__ == "__main__":
    # Create dictionary with three entries.
    values = {'a' : 1, 'b' : 2, 'c' : 3}

    # Raise exception
    #print(values['d'])

    # Avoid KeyError exception
    # return None
    print(values.get('d'))

    # get 'a'
    print(values.get('a'))
