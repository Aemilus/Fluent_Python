if __name__ == '__main__':
    symbols = '$¢£¥€¤'
    print('symbols:', symbols)

    codes = [ord(symbol) for symbol in symbols]
    print('codes:', codes)
