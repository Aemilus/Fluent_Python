if __name__ == '__main__':
    colors = ['black', 'white']
    sizes = ['S', 'M', 'L']
    tshirts = [(c, s) for c in colors for s in sizes]
    print('tshirts:', tshirts)
    # Output:
    # tshirts: [('black', 'S'), ('black', 'M'), ('black', 'L'), ('white', 'S'), ('white', 'M'), ('white', 'L')]

    for color in colors:
        for size in sizes:
            print((color, size))

    tshirts = [(c, s)
               for s in sizes
               for c in colors]
    print('tshirts:', tshirts)
