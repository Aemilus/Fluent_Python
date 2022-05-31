import dis


if __name__ == '__main__':
    bytecode = dis.dis('s[a] += b')
