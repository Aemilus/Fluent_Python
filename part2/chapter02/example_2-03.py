if __name__ == '__main__':
    symbols = '$¢£¥€¤'
    print('symbols:', symbols)

    beyond_ascii = [ord(symbol) for symbol in symbols if ord(symbol) > 127]
    print('beyond_ascii:', beyond_ascii)

    beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
    print('beyond_ascii:', beyond_ascii)
