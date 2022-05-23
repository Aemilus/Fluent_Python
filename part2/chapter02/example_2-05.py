import array

if __name__ == '__main__':
    symbols = '$¢£¥€¤'

    codes = tuple(ord(s) for s in symbols)
    print('type:', type(codes))
    print('codes:', codes)

    codes = array.array('I', (ord(s) for s in symbols))
    print('type:', type(codes))
    print('codes:', codes)
