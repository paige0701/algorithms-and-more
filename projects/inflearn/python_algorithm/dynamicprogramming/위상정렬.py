if __name__ == '__main__':

    import sys
    sys.stdin = open('./위상정렬.txt')
    n, m = map(int, input().split())
    degree = [0] * (m+1)
    from collections import deque
    queue = deque()
    graph = [[0 for _ in range(n+1)] for i in range(n+1)]

    for i in range(m):
        a, b = map(int, input().split())
        graph[a][b] = 1
        degree[b] += 1

    for i in range(1, len(degree)):
        if degree[i] == 0:
            queue.append(i)
    while queue:
        tmp = queue.popleft()
        print(tmp, end='')
        for i in range(n):
            if graph[tmp][i] == 1:
                degree[i] -=1
                if degree[i] == 0:
                    queue.append(i)





