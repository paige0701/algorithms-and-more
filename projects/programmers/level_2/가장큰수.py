if __name__ == '__main__':

    numbers = [6, 10, 2]

    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    print(str(int(''.join(numbers))))



