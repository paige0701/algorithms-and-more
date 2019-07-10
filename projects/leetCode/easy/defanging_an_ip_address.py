def test(address):
    return address.replace('.', '[.]')


if __name__ == '__main__':
    print(test('1.1.1.1'))
