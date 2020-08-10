
if __name__ == '__main__':

    import sys
    sys.stdin = open('./가방문제.txt', 'r')
    n, m = map(int, input().split())
    print(n, m)
    dy = [0] * (m+1)
    arr = []
    for i in range(n):
        w, v = map(int, input().split())
        for j in range(w, m+1):
            dy[j] = max(dy[j], dy[j - w] + v)
    print(dy[m])




