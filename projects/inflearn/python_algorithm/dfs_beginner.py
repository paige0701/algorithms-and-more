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


if __name__ == '__main__':
    one = One()
    # one.to_binary2(11)

    two = Two()
    two.pre_order_traversal(1)
    print()
    two.in_order_traversal(1)
    print()
    two.post_order_traversal(1)
