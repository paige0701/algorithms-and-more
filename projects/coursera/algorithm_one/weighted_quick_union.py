
"""

This is a lazy approach

"""
class QuickUnion:
    def __init__(self, num):
        self.result = []
        self.size = []
        for i in range(num):
            self.result.append(i)
            self.size.append(0)
        print(self.result)

    def root(self, i):
        while i != self.result[i]:
            self.result[i] = self.result[self.result[i]]
            i = self.result[i]
        return i

    def connected(self, a,b):
        return self.root(a) == self.root(b)

    def union(self, a,b):
        a1 = self.root(a)
        b1 = self.root(b)

        if a1 == b1:
            return
        if self.size[a1] < self.size[b1]:
            self.result[a1] = b1
            self.size[b1] += self.size[a1]
        else:
            self.result[b1] = a1
            self.size[a1] += self.size[b1]


if __name__ == '__main__':
    qu = QuickUnion(9)
    qu.union(4,3)
    qu.union(3,8)
    qu.union(6,5)
    qu.union(7,4)
    print(qu.connected(3,8))
