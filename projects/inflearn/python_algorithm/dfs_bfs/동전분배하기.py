def DFS(L):

    global res, c
    if L == len(c):
        char = max(money) - min(money)
        if char < res:
            tmp = set(money)
            if len(tmp) == 3:
                res = char
    else:
        for i in range(3):
            money[i] += c[L]
            DFS(L + 1)
            money[i] -= c[L] # 취소해야


if __name__ == '__main__':

    c = [8, 9, 11, 12, 23, 15, 17]
    res = 214700000
    money = [0] * 3
    DFS(0)
    print(res)
