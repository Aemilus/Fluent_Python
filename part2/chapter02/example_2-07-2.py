if __name__ == '__main__':
    # Using * to grab excess items
    a, b, *rest = range(5)
    print(a)
    print(b)
    print(rest)
    print()

    a, b, *rest = range(3)
    print(a)
    print(b)
    print(rest)
    print()

    a, b, *rest = range(2)
    print(a)
    print(b)
    print(rest)
    print()

    # in the context of parallel assignment, the * prefix can be applied to exactly one variable,
    # but it can appear in any position
    a, *body, c, d = range(5)
    print(a)
    print(body)
    print(c)
    print(d)
    print()

    *head, b, c, d = range(5)
    print(head)
    print(b)
    print(c)
    print(d)
