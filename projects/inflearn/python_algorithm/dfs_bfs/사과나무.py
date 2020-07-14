def BFS(n , a):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    ch = [[0] * n for _ in range(n)]
    sum = 0
    from collections import deque
    dq = deque()

    ch[n//2][n//2] = 1
    sum += a[n//2][n//2]

    dq.append((n//2, n//2))
    L = 0

    while True:
        if L == n//2:
            break
        size = len(dq)
        for i in range(size):
            tmp = dq.popleft()
            for j in range(4):
                x = tmp[0] + dx[j]
                y = tmp[1] + dy[j]
                if ch[x][y] == 0:
                    sum += a[x][y]
                    ch[x][y] = 1
                    dq.append((x, y))
        L += 1
    print(sum)


if __name__ == '__main__':
    n = 5
    a = [[10, 13, 10, 12, 15],
         [12, 39, 30, 23, 11],
         [11, 25, 50, 53, 15],
         [19, 27, 29, 37, 27],
         [19, 13, 30, 13, 19]
         ]
    BFS(n, a)
