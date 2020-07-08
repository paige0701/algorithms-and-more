def DFS(v):

    global n, s, a, g, ch, cnt, path
    if v == n:
        print(path)
        cnt += 1
    else:
        for i in range(1, n+1):
            if g[v][i] == 1 and ch[i] == 0:
                ch[i] = 1
                path.append(i)
                DFS(i)
                path.pop()
                ch[i] = 0


if __name__ == '__main__':
    n = 5
    s = 9
    a = [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 5], [3, 4], [4, 2], [4, 5]]
    g = [[0] * (n+1) for _ in range(n+1)]

    for i in a:
        a, b = i[0], i[1]
        g[a][b] = 1
    ch = [0] * (n+1)
    ch[1] = 1
    cnt = 0
    path = []
    path.append(1)
    DFS(1)
    print(cnt)


