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
    five.sort_meeting_room()