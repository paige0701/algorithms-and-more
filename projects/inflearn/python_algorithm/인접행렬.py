

if __name__ == '__main__':
    n, m = 5, 5
    g = [[0] * (n) for _ in range(n)]
    a = [[1, 2], [1, 3], [2, 4], [3, 4], [4, 5]]
    print(g)
    for i in a:
        o, t = i[0]-1, i[1]-1
        g[o][t] = 1
        g[t][o] = 1
    print(g)

    n, m, = 6, 9
    l = [[1, 2, 7], [1, 3, 4], [2, 1, 2], [2, 3, 5], [2, 5, 5], [3, 4, 5], [4, 2, 2], [4, 5, 5], [6, 4, 5]]
    r = [[0] * n for _ in range(n)]
    for i in l:
        a, b, c = i[0]-1, i[1]-1, i[2]
        r[a][b] = c

    for i in range(n):
        for j in range(n):
            print(r[i][j], end=' ')
        print()

