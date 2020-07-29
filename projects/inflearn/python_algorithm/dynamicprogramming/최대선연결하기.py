if __name__ == '__main__':
    n = 10
    arr = [4, 1, 2, 3, 9, 7,  5, 6, 10, 8]
    arr.insert(0, 0)
    dy = [0] * (n+1)
    dy[1] = 1
    res = 0
    for i in range(2, n+1):
        max = 0
        for j in range(i-1, 0, -1):
            if arr[j] < arr[i] and dy[j] > max:
                max = dy[j]
        dy[i] = max +1

        if dy[i] > res:
            res = dy[i]
    print(res)
