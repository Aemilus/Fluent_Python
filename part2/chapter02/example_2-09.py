from collections import namedtuple


# two parameters are required to create a named tuple: a class name and a list of field names,
# which can be given as an iterable of strings or as a single space delimited string
City = namedtuple('City', 'name country population coordinates')

if __name__ == '__main__':
    # data must be passed as positional arguments to the constructor
    # (in contrast, the tuple constructor takes a single iterable)
    tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
    # you can access the fields by name or position
    print('City instance:', tokyo)
    print('population:', tokyo.population)
    print('coordinates:', tokyo.coordinates)
    print('country:', tokyo[1])
