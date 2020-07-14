def BFS(n, m):  # TODO : BFS ! this is very clever! study this!

    from collections import deque

    max = 10000

    ch = [0] * (max+1)
    dis = [0] * (max+1)
    ch[n] = 1
    dis[n] = 0
    dq = deque()
    dq.append(n)

    while dq:

        now = dq.popleft()
        if now == m:
            break

        for next in (now-1, now+1, now+5):
            if 0 < next <= max:
                if ch[next] == 0:
                    dq.append(next)
                    ch[next] = 1
                    dis[next] = dis[now] + 1

    print(dis[m])


if __name__ == '__main__':

    s, e = 5, 14

    BFS(s, e)
