# study 0-1 knapsack algorithm!!

if __name__ == '__main__':
    import sys
    sys.stdin = open('./최대점수구하기.txt')

    n, m = map(int, input().split())
    ch = [[0] * (m + 1) for i in range(n + 1)]
    for i in range(1, n+1):
        v, t = map(int, input().split())
        for j in range(1, m+1):
            if j < t:
                ch[i][j] = ch[i-1][j]
            else:
                ch[i][j] = max((v + ch[i-1][j-t]), ch[i-1][j])
    print(ch[n][m])
