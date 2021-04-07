from timeit import Timer


def test1():
    l = []
    for i in range(1000):
        l = l + [i]


def test2():
    l = []
    for i in range(1000):
        l.append(i)


def test3():
    l = [i for i in range(1000)]


def test4():
    l = list(range(1000))


x = list(range(2000000))

if __name__ == '__main__':
    t1 = Timer('test1()', 'from __main__ import test1')
    print(f'concat -> {t1.timeit(number=1000):15.2f} milliseconds')

    t2 = Timer('test2()', 'from __main__ import test2')
    print(f'append -> {t2.timeit(number=1000):15.2f} milliseconds')

    t3 = Timer('test3()', 'from __main__ import test3')
    print(f'list comp -> {t3.timeit(number=1000):15.2f} milliseconds')

    t4 = Timer('test4()', 'from __main__ import test4')
    print(f'list range -> {t4.timeit(number=1000):15.2f} milliseconds')

    pop_zero = Timer('x.pop(0)', 'from __main__ import x')
    pop_end = Timer('x.pop()', 'from __main__ import x')

    print(f"pop(0): {pop_zero.timeit(number=1000):15.5f} milliseconds")
    print(f'pop(): {pop_end.timeit(number=1000):15.5f} milliseconds')
