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


if __name__ == '__main__':
    print(fib_memo(35))
    print(fib(35))
