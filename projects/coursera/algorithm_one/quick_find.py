"""
숫자가 연결 되어있는지 확인하는 방법.
먼저 빈 리스트에 인덱스 값으로 체운다. 두 숫자를 연걸하려고 하면 같은 인덱스 번호를 사용한다.
Simple as that.
제일 간단하게 푸는 방법이다.
이것을 가장 빠른 방법은 아니다.
"""

class QuickFind:
    def __init__(self, size):
        self.container = []
        for i in range(size):
            self.container.append(i)
        print(self.container)


    def union(self, num1, num2):
        a = num1
        b = num2
        for i, v in enumerate(self.container):
            if v == a:
                self.container[i] = b
        pass

    def is_connected(self, num1, num2):
        return self.container[num1] == self.container[num2]


if __name__ == '__main__':
    qf = QuickFind(9)
    qf.union(0, 5)
    qf.union(5, 6)
    qf.union(1, 2)
    qf.union(2, 7)
    qf.union(3, 4)
    print(qf.is_connected(0,1))