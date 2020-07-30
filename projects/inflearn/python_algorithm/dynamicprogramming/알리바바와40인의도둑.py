def DFS(x, y):
    if dy[x][y] > 0:
        return dy[x][y]

    if x == 0 and y == 0:
        return arr[x][y]
    else:
        if y == 0:
            dy[x][y] = DFS(x-1, y) + arr[x][y]
        elif x == 0:
            dy[x][y]= DFS(x, y-1) + arr[x][y]
        else:
            dy[x][y] = min(DFS(x, y-1), DFS(x-1, y)) + arr[x][y]
        return dy[x][y]


if __name__ == '__main__':
    import sys
    sys.stdin = open('./알리바바와40인의도둑.txt')
    n = int(input())
    arr = [list(map(int, input().split())) for i in range(n)]
    dy = [[0] * n for _ in range(n)]

    dy[0][0] = arr[0][0]

    for i in range(n):
        dy[0][i] = dy[0][i-1] + arr[0][i]
        dy[i][0] = dy[i-1][0] + arr[i][0]

    for i in range(1, n):
        for j in range(1, n):
            dy[i][j] = min(arr[i][j] + dy[i-1][j], arr[i][j] + dy[i][j-1])

    print(dy[n-1][n-1])


    # top down
    sys.stdin = open('./알리바바와40인의도둑.txt')
    n = int(input())
    arr = [list(map(int, input().split())) for i in range(n)]
    dy = [[0] * n for _ in range(n)]
    print(DFS(n-1, n-1))