def DFS(L, sum):
    global res, c

    if sum > T:
        return

    if L == k:
        if sum == T:
            res += 1
    else:
        for i in range(c[L][1]+1):
            DFS(L+1, sum + (c[L][0] * i))


if __name__ == '__main__':
    T = 20
    k = 3
    c = [[5, 3], [10, 2], [1, 5]]
    res = 0
    DFS(0, 0)
    print(res)
