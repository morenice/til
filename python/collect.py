import collections


c = collections.Counter('hello new python world')
print(c)

# mostly count
print(c.most_common(1))

# count 'h'
print(c['h'])
