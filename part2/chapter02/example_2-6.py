if __name__ == '__main__':
    colors = ('black', 'white')
    sizes = ('S', 'M', 'L')
    tshirts = ((c, s)
               for c in colors
               for s in sizes)
    print('type:', type(tshirts))
    print('Iterating over tshirts generator:')
    for t in tshirts:
        print(t)
