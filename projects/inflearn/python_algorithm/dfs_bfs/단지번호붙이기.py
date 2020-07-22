
def DFS(x, y):
    global cnt
    cnt += 1
    board[x][y] = 0

    for k in range(4):
        xx = x + dx[k]
        yy = y + dy[k]
        if 0 <= xx < n and 0 <= yy < n and board[xx][yy] == 1:
            DFS(xx, yy)


if __name__ == '__main__':
    import sys
    sys.stdin = open('./단지번호붙이기.txt')
    n = int(input())
    board = [list(map(int, input())) for _ in range(n)]

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    res = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                cnt = 0
                DFS(i, j)
                res.append(cnt)
    print(len(res))
    res.sort()
    for i in res:
        print(i)



