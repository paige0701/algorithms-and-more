if __name__ == '__main__':
    n = 7

    c = [0] * (n+1)
    c[0] = 1
    c[1] = 2

    for i in range(2,n+1):
        c[i] = c[i-1] + c[i-2]
    print(c[n])