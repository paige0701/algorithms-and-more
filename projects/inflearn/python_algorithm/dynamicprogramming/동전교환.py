def coin_change(level):

    global n, coins, m, res

    if level < 0:
        print(sum(res))
    else:
        res[level] = m // coins[level]
        m = m - (coins[level] * res[level])

        coin_change(level-1)


if __name__ == '__main__':
    import sys
    sys.stdin = open('./동전교환.txt')
    n = int(input())
    coins = list(map(int, input().split(' ')))
    # coins.sort() # 정렬
    #
    m = int(input())
    #
    # res = [0] * (n+1)

    # coin_change(n - 1)

    dy = [1000] * (m+1)
    dy[0] = 0
    for i in coins:
        for j in range(i, m+1):
             dy[j] = min(dy[j], dy[j-i] + 1)

    print(-1 if dy[m] == 1000 else dy[m])

