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


class Five:

    total = 100000000
    a = [27, 567,999,234, 50, 567, 123,4734, 754, 84, 35,1353, 76, 464,4634, 65, 89 , 3553, 59, 38, 4135]
    diff = -21167888

    def solution(self, n, tot, tsum):

        if tot + (sum(self.a)-tsum) < self.diff: # this is important less time
            return

        if n == len(self.a):
            if self.total > tot > self.diff:
                self.diff = tot

        else:
            self.solution(n+1, tot + self.a[n], tsum+self.a[n])
            self.solution(n+1, tot, tsum+self.a[n])


class Six:

    n, m = 3, 2
    result = [0] * n
    cnt = 0

    def solution(self, l):
        if l == self.m:
            for i in range(self.m):
                print(self.result[i], end=' ')
            print()
            self.cnt += 1
        else:
            for i in range(1, self.n+1):

                self.result[l] = i
                self.solution(l+1)


class Eight:
    m = 2
    n = 3
    res = [0] * n
    ch = [0] * (n+1)

    def solution(self, L):
        if L == self.m:
            for i in range(L):
                print(self.res[i], end='')
            print()
        else:
            for i in range(1, self.n+1):
                if self.ch[i] == 0:
                    self.ch[i] = 1
                    self.res[L] = i
                    self.solution(L+1)
                    self.ch[i] = 0


class Nine:
    n = 4
    m = 16
    res = [0] * n
    ch = [0] * (n+1)
    t = [1, 3, 3, 1]

    def solution(self, L):
        if L == self.n:
            t = 0
            for i in range(len(self.res)):
                t += (self.res[i] * self.t[i])
            if t == self.m:
                print(''.join([str(i) for i in self.res]))
                import sys
                sys.exit(0)

        else:
            for i in range(1, self.n+1):
                if self.ch[i] == 0:
                    self.ch[i] = 1
                    self.res[L] = i
                    self.solution(L+1)
                    self.ch[i] = 0


    n, f = 4, 16
    p = [0] * n
    b = [1] * n
    ch = [0] * (n+1)

    #  TODO: 1,3,3,1 이항계수 구하는 법 !! 주용함
    for i in range(1, n):
        b[i] = b[i - 1] * (n - i) // i

    # TODO: itertools.permutaions
    def solution2(self, L, sum):

        if L == self.n and sum == self.f:
            for x in self.p:
                print(x, end=' ')
            import sys
            sys.exit(0)

        else:
            for i in range(1, self.n+1):
                if self.ch[i] == 0:
                    self.ch[i] = 1
                    self.p[L] = i
                    self.solution2(L+1, sum + (self.p[L] * self.b[L]))
                    self.ch[i] = 0


class Ten:
    n, m = 4, 2
    res = [0] * m
    cnt = 0
    def solution(self, L, s):
        if L >= m:
            for i in self.res:
                print(i, end='')
            print()
            self.cnt+=1
        else:
            for i in range(s, self.n+1):
                self.res[L] = i
                self.solution(L+1, i+1)


class Eleven:
    n, k, m = 5, 3, 6
    a = 2, 4, 5, 8, 12
    res = [0] * n
    cnt = 0

    # find combinations using itertools
    import itertools  # combinations
    # for x in itertools.combinations(a, k):


    def solution(self, L, s, total):
        if L == self.k:
            if total % self.m == 0:
                self.cnt += 1
        else:
            for i in range(s, self.n):
                self.res[L] = self.a[i]
                self.solution(L+1, i+1, total+self.a[i])


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
    # four.DFS(0, 0)


    # five = Five()
    # five.solution(0,0, 0)
    # print(five.diff)

    six = Six()
    # six.solution(0)
    # print(six.cnt)

    # seven = Seven()

    a = [419, 408, 186, 83]
    a.sort(reverse=True)
    money = 6249
    res = 21470000
    # print(seven.solution(len(a)-1))
    # seven.DFS(0,0)
    # print(res)
    # print(seven.coinChange([186,419,83,408], 6249))

    m = 2
    # n = 3
    # eight = Eight()
    # eight.solution(0)

    nine = Nine()
    # nine.solution(0)
    # nine.solution2(0,0)

    ten = Ten()
    # ten.solution(0,1)
    # print(ten.cnt)

    el = Eleven()
    el.solution(0, 0, 0)
    print(el.cnt)
