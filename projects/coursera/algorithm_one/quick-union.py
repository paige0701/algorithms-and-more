
"""

This is a lazy approach

"""
class QuickUnion:
    def __init__(self, num):
        self.result = []
        for i in range(num):
            self.result.append(i)
        print(self.result)

    def root(self, i):
        while i != self.result[i]:
            i = self.result[i]
        return i

    def connected(self, a,b):
        return self.root(a) == self.root(b)

    def union(self, a,b):
        a1 = self.root(a)
        b1 = self.root(b)
        self.result[a1] = b1

if __name__ == '__main__':
    qu = QuickUnion(9)
    qu.union(8,0)
    qu.union(2,1)
    qu.union(1,8)
    print(qu.connected(0,5))
