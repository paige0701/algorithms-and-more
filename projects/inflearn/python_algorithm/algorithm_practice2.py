class One:

    @staticmethod
    def get_list():
        import sys
        sys.stdin = open('is_palindrome.txt', 'rt')
        n = int(input())

        li = []
        for i in range(n):
            li.append(input())
        return li

    def is_palindrome(self, li):

        if len(li) == 0 or len(li) == 1:
            return 'yes'
        elif li[0].lower() != li[-1].lower():
            return 'No'
        else:
            return self.is_palindrome(li[1:-1])

    @staticmethod
    def is_palindrome3(s):
        s = s.lower()
        print(s == s[::-1])

    @staticmethod
    def is_palindrome2(s):

        s = s.lower()
        size = len(s)
        for i in range(size//2):

            if s[i] != s[-1-i]:
                print('No')
                break
        else:
            print('Yes')


class Two:

    @staticmethod
    def extract_only_numbers_and_print_its_divisors():

        import sys
        sys.stdin = open('extract_numbers.txt', 'rt')
        s = input()
        li = ''
        for i in s:
            try:
                s = int(i)
                li += str(s)
            except:
                pass
        print(int(li))

        cnt = 0
        for i in range(1, int(li)+1):
            if int(li) % i == 0:
               cnt += 1
        print(cnt)

    @staticmethod
    def solution():
        import sys
        sys.stdin = open('extract_numbers.txt', 'rt')
        s = input()
        res = 0
        for i in s:
            if i.isdecimal():
               res = res * 10 + int(i)

        print(res)
        cnt = 0
        for i in range(1, res+1):
            if res % i == 0:
                cnt +=1
        print(cnt)


class Three:

    @staticmethod
    def list_comprehension():

        li = list(range(1, 21))
        print(li)
        import sys
        sys.stdin = open('list_comp/three.txt', 'rt')
        for _ in range(10):
            x, y = map(int, input().split())
            temp = li[x-1: y]
            temp.reverse()
            li = li[:x-1] + temp + li[y:]
        print(li)

    @staticmethod
    def solution():
        a = list(range(21))
        import sys
        sys.stdin = open('list_comp/three.txt', 'rt')
        for _ in range(10):
            s, e = map(int, input().split())
            for i in range((e-s+1)//2):
                a[s+i], a[e-i] = a[e-i], a[s+i]
        a.pop(0)
        print(a)


class Four:

    @staticmethod
    def combine_two_list_and_sort():  # this is nlog(n)

        import sys
        sys.stdin = open('list_comp/four.txt')
        n = input()
        a = list(map(int, input().split()))
        m = input()
        b = list(map(int, input().split()))

        c = a +b
        c.sort()
        print(c)

    @staticmethod
    def solution():  # this is O(n)
        import sys
        sys.stdin = open('list_comp/four.txt')
        n = int(input())
        a = list(map(int, input().split()))
        m = int(input())
        b = list(map(int, input().split()))
        c = []
        p1 = p2 = 0

        while p1 < n and p2< m:
            if a[p1] <= b[p2]:
                c.append(a[p1])
                p1 += 1
            else:
                c.append(b[p2])
                p2 += 1

        if p1 < n:
            c += a[p1:]
        if p2 < m:
            c += b[p2:]
        print(c)


class Five:

    @staticmethod
    def sum_of_numbers():
        import sys
        sys.stdin = open('list_comp/five.txt')
        n, m = map(int, input().split())
        a = list(map(int, input().split()))
        cnt = 0
        tot = a[0]
        lt, rt = 0, 1

        while True:

            if tot < m:
                if rt < n:
                    tot += a[rt]
                    rt += 1
                else:
                    break

            elif tot == m:
                cnt += 1
                tot -= a[lt]
                lt += 1
            else:
                tot -= a[lt]
                lt += 1
        print(cnt)


class Six:
    @staticmethod
    def find_max_sum_from_grating():

        import sys
        sys.stdin = open('list_comp/six.txt')
        n = int(input())

        a = [list(map(int, input().split())) for _ in range(n)]
        print(a)

        sum_of_numbers = 0

        d1 = 0
        d2 = 0
        for i, v in enumerate(a):
            temp = 0
            for j, value in enumerate(v):
                temp += a[j][i]
            if sum_of_numbers < sum(v):
                sum_of_numbers = sum(v)

            if sum_of_numbers < temp:
                sum_of_numbers = temp

            d1 += a[i][n-i-1]
            d2 += a[i][i]

        print(max(sum_of_numbers, d1, d2))


class Seven:

    # 다이아몬드 printing
    @staticmethod
    def find_sum_from_two_dimensional_array():

        import sys
        sys.stdin = open('list_comp/seven.txt')
        n = int(input())
        a = [list(map(int, input().split())) for _ in range(n)]
        res = 0
        s = e = n//2
        for i in range(n):
            for j in range(s, e+1):
                res += a[i][j]
            if i < n//2:
                s -= 1
                e += 1
            else:
                s += 1
                e -= 1
        print(res)


class Eight:

    @staticmethod
    def hour_glass():
        import sys
        sys.stdin = open('list_comp/eight.txt')
        n = int(input())
        a = [list(map(int, input().split())) for _ in range(n)]
        m = int(input())
        b = [list(map(int, input().split())) for _ in range(m)]

        for i in b:
            for j in range(i[2]):
                if i[1] == 1:
                    b = a[i[0]-1].pop()
                    a[i[0] - 1].insert(0, b)
                else:
                    b = a[i[0]-1].pop(0)
                    a[i[0] - 1].append(b)
        l = 0
        r = n-1
        total = 0
        for i in range(n):
            if l <= r:
                for j in range(l, r + 1):
                    total += a[i][j]
            else:
                for j in range(r, l+1):
                    total += a[i][j]
            l += 1
            r -= 1
        print(total)

    @staticmethod
    def solution():
        import sys
        sys.stdin = open('list_comp/eight.txt')
        n = int(input())
        a = [list(map(int, input().split())) for _ in range(n)]
        m = int(input())
        for i in range(m):
            h, t, k = map(int, input().split())
            if t == 0:
                for _ in range(k):
                    a[h-1].append(a[h-1].pop(0))
            else:
                for _ in range(k):
                    a[h-1].insert(0, a[h-1].pop())

        res = 0
        s = 0
        e = -1
        for i in range(n):
            for j in range(s, e+1):
                res += a[i][j]
            if i < n//2:
                s+=1
                e-=1
            else:
                s-=1
                e+=1


class Nine:

    @staticmethod
    def find_humps():
        import sys
        sys.stdin = open('list_comp/nine.txt', 'rt')
        n = int(input())
        a = []
        for i in range(n):
            a.append(list(map(int, input().split())))
            a[i].insert(0, 0)
            a[i].append(0)
        p = [0] * 7
        a.insert(0, p)
        a.append(p)

        cnt = 0
        print(a)
        for i in range(1, n+1):
            for j in range(1, n+1):
                if all(k < a[i][j] for k in [a[i-1][j], a[i][j+1], a[i+1][j], a[i][j-1]]):
                    cnt += 1
        print(cnt)

    @staticmethod
    def solution():
        import sys
        sys.stdin = open('list_comp/nine.txt')
        n = int(input())
        a = [list(map(int, input().split())) for _ in range(n)]
        a.insert(0, [0] * n)
        a.append([0]*n)

        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        for x in a:
            x.insert(0, 0)
            x.append(0)
        cnt = 0
        for i in range(1, n+1):
            for j in range(1, n+1):
                if all(a[i][j] > a[i+dx[k]][j+dy[k]] for k in range(4)):
                    cnt += 1


class Ten:

    def check_sudoku(self):

        import sys
        sys.stdin = open('list_comp/ten.txt')
        a = [list(map(int, input().split())) for _ in range(9)]

        # 행과 열을 체크
        for i in range(9):
            ch1 = [0] * 10
            ch2 = [0] * 10
            for j in range(9):
                ch1[a[i][j]] = 1
                ch2[a[j][i]] = 1
            if sum(ch1) != 9 or sum(ch2) != 9:
                return False

        for i in range(3):
            for j in range(3):
                ch3 = [0]*10
                for k in range(3):
                    for s in range(3):
                        ch3[a[i*3+k][j*3+s]] = 1
                if sum(ch3) != 9:
                    return False
        return True


if __name__ == '__main__':

    one = One()

    # for i in one.get_list():
    #     one.is_palindrome3(i)

    two = Two()
    # two.solution()

    three = Three()
    # three.list_comprehension()

    # three.solution()

    four = Four()
    # four.solution()

    five = Five()
    # five.sum_of_numbers()

    six = Six()
    # six.find_max_sum_from_grating()

    seven = Seven()
    # seven.find_sum_from_two_dimensional_array()

    eight = Eight()
    # eight.hour_glass()

    nine = Nine()
    # nine.solution()

    ten = Ten()
    print(ten.check_sudoku())
