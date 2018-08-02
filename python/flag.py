# By Real Python
#
a, b, c = True, False, False

if a is True or b is True or c is True:
    print('is True OK!')

if any((a, b, c)):
    print('any True OK!')

if True in (a, b, c):
    print('in [a, b, c] True OK!')
