from collections import deque

if __name__ == '__main__':
    import sys
    sys.stdin = open('./토마토.txt')
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(m)]
    Q = deque()
    dis = [[0] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            if board[i][j] == 1:
                Q.append((i, j))

    while Q:
        tmp = Q.popleft()
        for i in range(4):
            xx = tmp[0] + dx[i]
            yy = tmp[1] + dy[i]
            if 0 <= xx < m and n > yy >= 0 == board[xx][yy]:
                board[xx][yy] = 1
                dis[xx][yy] = dis[tmp[0]][tmp[1]] + 1
                Q.append((xx, yy))


    flag = 1
    for i in range(m):
        for j in range(n):
            if board[i][j] == 0:
                flag = 1
    result = 0
    if flag == 1:
        for i in range(m):
            for j in range(n):
                if dis[i][j] > result:
                    result = dis[i][j]
        print(result)
    else:
        print(-1)
