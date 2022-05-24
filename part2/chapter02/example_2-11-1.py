if __name__ == '__main__':
    # 1
    print("Original list:")
    k = list(range(10))
    print(k)

    # 2
    print('After k[2:5] = [20, 30]:')
    k[2:5] = [20, 30]
    print(k)

    # 3
    print('After del(k[5:7]):')
    del(k[5:7])
    print(k)

    # 4
    print('After k[3::2] = [11, 22]:')
    k[3::2] = [11, 22]
    print(k)

    # 5
    # When the target of the assignment is a slice,
    # the right side must be an iterable object,
    # even if it has just one item.
    print('Try k[2:5] = 100:')
    try:
        k[2:5] = 100
    except TypeError as e:
        print(e)

    print('Try k[2:5] = [100]:')
    k[2:5] = [100]
    print(k)

    # 6
    print('After k[:-2] = [99, 88]')
    k[:-2] = [99, 88]
    print(k)
