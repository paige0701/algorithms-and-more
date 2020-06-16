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


if __name__ == '__main__':
    one = One()
    # one.binary_search()

    two = Two()
    # two.decision_algorithm()

    three = Three()
    three.solution()