from collections import namedtuple


City = namedtuple('City', 'name country population coordinates')
LatLong = namedtuple('LatLong', 'lat long')

if __name__ == '__main__':
    # _fields is a tuple with the field names of the class
    print('City fields:', City._fields)

    delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
    # _make() allow you to instantiate a named tuple from an iterable
    delhi = City._make(delhi_data)  # same as: delhi = City(*delhi_data)
    # _asdict() returns a collections.OrderedDict built from the named tuple instance
    for k, v in delhi._asdict().items():
        print(f"{k}: {v}")
