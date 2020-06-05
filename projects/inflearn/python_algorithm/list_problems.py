import random as r


def solution():

    a = []
    b = list()
    c = [1, 2, 33]

    print(a, b, c)
    r.shuffle(c)
    print(c)
    c.sort(reverse=True)
    print(c)

    if all(60 > x for x in c):
        print('all numbers are less than 60')
    else:
        print('at least one number is bigger than 60')

    if any(60 < x for x in c):
        print('at least one is bigger than 60')
    else:
        print('Nothing is bigger than 60')

    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 로 초기화
    a = [0] * 10
    print(a)

    b = [[0] * 3 for _ in range(3)]
    print(b)


class WhatIsLambda:

    # 익명의 함수 - 이름이 없는 함수다 - 표현식이라고도 부름
    @staticmethod
    def plus_one(x):
        return x + 1

    def lambda_func(self):

        a = [1, 2, 3]
        print(list(map(self.plus_one, a)))
        print(list(map(lambda x: x*2, a)))


if __name__ == '__main__':
    solution()

    lam = WhatIsLambda()
    print(lam.plus_one(3))
    lam.lambda_func()

