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