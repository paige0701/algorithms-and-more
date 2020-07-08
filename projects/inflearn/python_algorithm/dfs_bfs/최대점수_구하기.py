def DFS(L, s, t):
    global res, n, m
    if t > m:
        return
    if L == n:
        if s > res:
            res = s
    else:
        DFS(L+1, s+pv[L], t + pt[L])  # yes
        DFS(L+1, s, t)                # no


if __name__ == '__main__':
    n, m = 5, 20
    pv = list()
    pt = list()
    a = [[10, 5], [25, 12], [15, 8], [6, 3], [7, 4]]
    res = -214700000
    for i in a:
        pv.append(i[0])
        pt.append(i[1])
    DFS(0, 0, 0)
    print(res)