def DFS(L, price):
    global n, res, t, p

    if L == n+1:
        if price > res:
            res = price
    else:

        if L + t[L] > n+1:
            DFS(L+1, price)
        else:
            DFS(L + t[L], price + p[L])


if __name__ == '__main__':
    n = 7
    a = [[4, 20], [2, 10], [3, 15], [3, 20], [2, 30], [2, 20], [1, 10]]
    t = list()
    p = list()

    for i in a:
        t.append(i[0])
        p.append(i[1])
    res = -214700000
    t.insert(0, 0)
    p.insert(0, 0)
    DFS(1, 0)
    print(res)
