if __name__ == '__main__':
    # latitude and longitude of the Los Angeles International Airport
    airport_coordinates = (33.9425, -118.408056)
    latitude, longitude = airport_coordinates
    print('latitude:', latitude)
    print('longitude', longitude)
    print()

    # swapping variables
    print(f"a\tb")
    a = 5
    b = 10
    print(f"{a}\t{b}")
    b, a = a, b
    print(f"{a}\t{b}")
    print()

    # tuple unpacking with *
    t = (20, 8)
    r = divmod(*t)
    print(r)
    print()

    # sometimes when we only care about certain parts of a tuple when unpacking
    # a dummy variable like _ is used as placeholder
    date = (2022, 5, 21)
    year, _, _ = date
    print('year:', year)
    