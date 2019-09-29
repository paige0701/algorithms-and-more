def fib(idx, prev, next):
    if idx == 7:
        return next

    idx = idx + 1
    sum = prev + next
    return fib(idx, next, sum)

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)


if __name__ == '__main__':
    fib(7)