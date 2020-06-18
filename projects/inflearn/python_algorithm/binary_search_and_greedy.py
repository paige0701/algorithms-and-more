class One:
    @staticmethod
    def binary_search():
        import sys
        sys.stdin = open('bs_and_greedy/one.txt')
        n, m = map(int, input().split())
        a = list(map(int, input().split()))
        a.sort()

        lt = 0
        rt = n-1
        while lt <= rt:
            mid = (lt+rt)//2
            if a[mid] == m:
                print(mid+1)
                break
            elif a[mid] > m:
                rt = mid-1
            else:
                lt = mid+1


class Two:

    @staticmethod
    def count(n, line):
        cnt = 0
        for i in line:
            cnt += (i//n)
        return cnt

    def decision_algorithm(self):
        import sys
        sys.stdin = open('bs_and_greedy/two.txt')
        k, n = map(int, input().split())
        line = []
        res = 0
        largest = 0
        for i in range(k):
            tmp = int(input())
            line.append(tmp)
            largest = max(largest, tmp)
        lt = 1
        rt = largest
        while lt <= rt:
            mid = (lt + rt)//2
            if self.count(mid, line) >= n:
                res = mid
                lt = mid+1
            else:
                rt = mid-1
        print(res)


class Three:

    def count(self, n, music):

        cnt = 1
        sum = 0
        for x in music:
            if sum + x > n:
                sum = x
                cnt += 1
            else:
                sum += x

        return cnt

    def solution(self):

        import sys
        sys.stdin = open('bs_and_greedy/three.txt')
        n, m = map(int, input().split())
        a = list(map(int, input().split()))
        lt = 1
        rt = sum(a)
        maxx = max(a)
        while lt <= rt:
            mid = (lt+rt)//2
            # one cd capacity must be bigger than biggest music
            if mid >= maxx and self.count(mid, a) <= m:
                res = mid
                rt = mid-1
            else:
                lt = mid+1
        print(res)


class Four:

    def count(self, mid, li):

        res = 1
        ep = li[0]
        for i in range(1, len(li)):
            if li[i] - ep >= mid:
                res += 1
                ep = li[i]
        return res

    def solution(self):
        import sys
        sys.stdin = open('bs_and_greedy/four.txt')
        n, c = map(int, input().split())
        a = [int(input()) for _ in range(n)]
        a.sort()

        lt = 1
        rt = a[n-1]
        while lt <= rt:
            mid = (lt+rt) // 2
            if self.count(mid, a) >= c:
                res = mid
                lt = mid + 1
            else:
                rt = mid-1
        print(res)


class Five:
    def sort_meeting_room(self):

        # 끝나는 시간으로 정렬을 해야한다!!!

        import sys
        sys.stdin = open('bs_and_greedy/five.txt')
        n = int(input())
        li = []
        for i in range(n):
            a, b = map(int, input().split())
            li.append((a, b))
        li.sort(key=lambda x: x[1])

        # cnt = 1
        # r = li[0][1]
        # for i in range(1, len(li)):
        #     if li[i][0] >= r:
        #         r = li[i][1]
        #         print(li[i])
        #         cnt += 1
        # print(cnt)
        cnt = 0
        et = 0
        for s, e in li:
            if s >= et:
                et = e
                cnt += 1
        print(cnt)


class Six:
    @staticmethod
    def solution():
        import sys
        sys.stdin = open('bs_and_greedy/six.txt')
        n = int(input())
        l = []
        for i in range(n):
            h, w = map(int, input().split())
            l.append((h, w))
        l.sort(reverse=True)
        cnt = 1
        for i in range(1,n):
            for j in range(i-1, -1, -1):
                if l[i][1] < l[j][1]:
                    break
            else:
                cnt += 1
        print(cnt)

    @staticmethod
    def solution2():
        import sys
        sys.stdin = open('bs_and_greedy/six.txt')
        n = int(input())
        l = []
        largest = 0
        for i in range(n):
            h, w = map(int, input().split())
            l.append((h, w))
        l.sort(reverse=True)
        cnt = 0
        for i, v in l:
            if largest < v:
                largest = v
                cnt += 1
        print(cnt)


class Seven:
    def solution(self):
        import sys
        sys.stdin = open('bs_and_greedy/seven.txt')
        l = int(input())
        a = list(map(int, input().split()))
        m = int(input())
        a.sort()
        print(a)
        for i in range(m):
            b = max(a)
            a[a.index(b)] = a[a.index(b)]-1
            s = min(a)
            a[a.index(s)] = a[a.index(s)] + 1

        print(a)
        b = max(a)
        s = min(a)

        print(b-s)

    @staticmethod
    def solution2():
        import sys
        sys.stdin = open('bs_and_greedy/seven.txt')
        L = int(input())
        a = list(map(int, input().split()))
        m = int(input())
        a.sort()
        for _ in range(m):
            a[0] += 1
            a[-1] -= 1
            a.sort()

        print(a[-1] - a[0])


class Eight:
    @staticmethod
    def solution():
        import sys
        sys.stdin = open('bs_and_greedy/eight.txt')
        N, M = map(int, (input().split()))
        a = list(map(int, input().split()))
        a.sort()
        lt = 0
        rt = N-1
        cnt = 0
        while lt <= rt:

            if a[lt] + a[rt] > M :
                cnt += 1
                rt -= 1
            elif a[lt] + a[rt] <= M:
                cnt += 1
                rt-=1
                lt+=1

        print(cnt)

    @staticmethod
    def solution2():
        import sys
        sys.stdin = open('bs_and_greedy/eight.txt')
        n, limit = map(int, (input().split()))
        p = list(map(int, input().split()))
        p.sort()
        cnt = 0
        while p:

            if len(p) == 1:
                cnt+= 1
                break

            if p[0] + p[-1] > limit:
                p.pop()
                cnt += 1
            else:
                p.pop(0)
                p.pop()
                cnt += 1
        print(cnt)

    @staticmethod
    def solution3():  # .pop(0) 을 하면 비 효율적이기 떄문에 list 대신 deque를 쓴다.
        from collections import deque
        import sys
        sys.stdin = open('bs_and_greedy/eight.txt')
        n, limit = map(int, (input().split()))
        p = list(map(int, input().split()))
        p.sort()
        p = deque(p)
        cnt = 0
        while p:
            if len(p) == 1:
                cnt += 1
                break

            if p[0] + p[-1] > limit:
                p.pop()
                cnt += 1
            else:
                p.popleft()
                p.pop()
                cnt += 1
        print(cnt)


class Nine:
    def solution(self):
        import sys
        sys.stdin = open('bs_and_greedy/nine.txt')
        n = int(input())
        a = list(map(int, input().split()))
        lt = 0
        rt = n-1
        last = 0
        res = ''
        tmp = []

        while lt<=rt:
            if a[lt] > last :
                tmp.append((a[lt], 'L'))
            if a[rt] > last:
                tmp.append((a[rt], 'R'))
            tmp.sort()

            if len(tmp) == 0:
                 break
            else:
                res = res + tmp[0][1]
                last = tmp[0][0]
                if tmp[0][1] == 'L' :
                    lt += 1
                else:
                    rt -=1

            tmp.clear()
        print(res)


if __name__ == '__main__':
    one = One()
    # one.binary_search()

    two = Two()
    # two.decision_algorithm()

    three = Three()
    # three.solution()

    four = Four()
    # four.solution()

    five = Five()
    # five.sort_meeting_room()

    six = Six()
    # six.solution2()

    seven = Seven()
    # seven.solution2()

    eight = Eight()
    # eight.solution3()

    nine = Nine()
    nine.solution()