# study 0-1 knapsack algorithm!!

if __name__ == '__main__':
    import sys
    sys.stdin = open('./최대점수구하기.txt')

    n, m = map(int, input().split())

    """
    using 2 dimensional arrays. -> very slow and takes up a lot of memory 
    ch = [[0] * (m + 1) for i in range(n + 1)]
    for i in range(1, n+1):
        v, t = map(int, input().split())
        for j in range(1, m+1):
            if j < t:
                ch[i][j] = ch[i-1][j]
            else:
                ch[i][j] = max((v + ch[i-1][j-t]), ch[i-1][j])
    print(ch[n][m])
    """

    # using 1 dimensional array
    dy = [0] * (m+1)
    for i in range(n):
        v, t = map(int, input().split())
        for j in range(m, t-1, -1):
            dy[j] = max(dy[j-t]+v, dy[j])
    print(dy[m])


