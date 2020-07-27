def DFS(x, y):
    global board, ch

    if x == 0:
        print(y)
    else:
        ch[x][y] = 1
        if y-1 >= 0 and board[x][y-1] == 1 and ch[x][y-1] == 0:
            DFS(x, y-1)
        elif y+1 <= 9 and board[x][y+1] == 1 and ch[x][y+1] != 1:
            DFS(x, y+1)
        else:
            DFS(x-1, y)


if __name__ == '__main__':
    import sys
    sys.stdin = open('./사다리타기.txt')
    board = [list(map(int, input())) for _ in range(10)]
    ch = [[0] * 10 for _ in range(10)]
    for i in range(len(board[9])):
        if board[9][i] == 2:
            s = (9, i)
    DFS(s[0], s[1])



