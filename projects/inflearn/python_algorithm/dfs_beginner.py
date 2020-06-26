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


if __name__ == '__main__':
    one = One()
    one.to_binary2(11)