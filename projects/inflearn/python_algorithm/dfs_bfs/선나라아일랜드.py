def solution(n, board):
    from collections import deque
    cnt = 0
    dx = [-1, 0, 1,  0, -1, 1, 1, -1]
    dy = [0 , 1, 0, -1, -1, 1, -1, 1]
    dq = deque()

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                board[i][j] = 0
                dq.append((i, j))
                while dq:
                    tmp = dq.popleft()
                    for k in range(8):
                        xx = tmp[0] + dx[k]
                        yy = tmp[1] + dy[k]
                        if 0 <= xx < n and 0 <= yy < n and board[xx][yy] == 1:
                            board[xx][yy] = 0
                            dq.append((xx, yy))
                cnt += 1
    print(cnt)


if __name__ == '__main__':
    import sys
    sys.stdin = open('./섬나라아일랜드.txt')
    n = int(input())
    board = [list(map(int, input())) for _ in range(n)]
    print(board)
    solution(n, board)