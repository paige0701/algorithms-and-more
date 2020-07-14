def DFS(L, P):
    global a, cnt, res, n

    if L == n:
        cnt += 1
        for j in range(P):
            print(chr(res[j]+96), end='')
        print()
    else:
        for i in range(1, 27):
            if a[L] == i:
                res[P] = i
                DFS(L+1, P+1)
            elif i >= 10 and a[L] == i//10 and a[L+1] == i%10:
                res[P] = i
                DFS(L+2, P+1)


if __name__ == '__main__':
    a = [2, 5, 1, 1, 2]
    n = len(a)
    a.append(-1)
    cnt = 0
    res = [0] * (n + 3)
    DFS(0, 0)
    print(cnt)
