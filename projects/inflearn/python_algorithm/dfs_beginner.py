class One:
    def to_binary(self, n):
        if n == 1:
            print(n, end='')
        else:
            self.to_binary(n // 2)
            print(n % 2, end='')

    def to_binary2(self,n):
        if n== 0:
            return
        else:
            self.to_binary2(n//2)
            print(n%2, end='')


class Two:
    def pre_order_traversal(self, v):
        if v > 7:
            return
        else:
            print(v, end='')
            self.pre_order_traversal(v*2)
            self.pre_order_traversal(v*2 +1)

    def in_order_traversal(self, v):
        if v > 7:
            return
        else:
            self.in_order_traversal(v * 2)
            print(v, end='')
            self.in_order_traversal(v * 2 + 1)

    def post_order_traversal(self, v):
        if v > 7:
            return
        else:
            self.post_order_traversal(v * 2)
            self.post_order_traversal(v * 2 + 1)
            print(v, end='')


class Three:

    n = 3
    ch = [0] * (n + 1)

    def DFS(self, v):
        if v == self.n+1:
            for i in range(1, self.n+1):
                if self.ch[i] == 1:
                    print(i, end='')
            print()

        else:
            self.ch[v] = 1
            self.DFS(v+1)
            self.ch[v] = 0
            self.DFS(v+1)


class Four:
    n = 6
    a = [1, 3, 5, 6, 7, 10]
    total = sum(a)
    my_sum = 0

    def DFS(self, v, total):
        print('sum ch = ', total)
        print('sum total = ', self.total)

        if total > self.total//2:
            return

        if v == self.n:
            if total == (self.total - total):
                print('Yes')
                import sys
                sys.exit(0)
        else:
            self.DFS(v + 1, total + self.a[v])
            self.DFS(v + 1, total)



if __name__ == '__main__':
    one = One()
    # one.to_binary2(11)

    two = Two()
    # two.pre_order_traversal(1)
    # print()
    # two.in_order_traversal(1)
    # print()
    # two.post_order_traversal(1)

    three = Three()
    # three.DFS(1)

    four = Four()
    four.DFS(0, 0)
