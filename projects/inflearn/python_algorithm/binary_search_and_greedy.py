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


if __name__ == '__main__':
    one = One()
    one.binary_search()
