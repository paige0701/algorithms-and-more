def fib(n):

    # this is O(n^2)
    if n == 1 or n == 2:
        return 1
    else:
        result = fib(n-1) + fib(n-2)
        return result


def fib2(n, memo):
    if memo[n] is not None:
        return memo[n]
    if n == 1 or n ==2:
        result = 1
    else:
        result = fib2(n-1, memo) + fib2(n-2, memo)
    memo[n]= result
    return result

def fib_memo(n):
    memo = [None] * (n+1)
    return fib2(n,memo)

def fib3_bottom_up(n):
    if n == 1 or n == 2:
        return 1
    bottom_up = [None] * (n+1)
    bottom_up[1] = 1
    bottom_up[2] = 1
    for i in range(3, n+1):
        bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]
    return bottom_up[n]


if __name__ == '__main__':
    print(fib_memo(35))
    # print(fib(35))
    print(fib3_bottom_up(35))
