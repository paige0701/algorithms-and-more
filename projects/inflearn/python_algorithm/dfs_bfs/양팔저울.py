def DFS(L, sum):
    global res
    if L == n:
        if 0 < sum <=s:
            res.add(sum)
    else:
        DFS(L+1, sum+G[L])
        DFS(L+1, sum-G[L])
        DFS(L+1, sum)


if __name__ == '__main__' :
    n = 3
    G = [1, 5, 7]
    s = sum(G)
    res = set()
    DFS(0, 0)
    print(s-len(res))