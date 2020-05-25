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


# 피보나치
# 0 1 1 2 3 5 8 13 21
# 순회 전      a = 0, b = 1  1
# 첫번째 순회   a = 1, b = 1  1
# 두번째 순회   a = 1, b = 2  2
# 세번쨰 순회   a = 2, b = 3  3
# 네번째 순회   a = 3, b = 5  5
# 다섯번째 순회  a = 5, b = 8  8
"""

a = 0
b = 1
print(a)
for i in range(10):
    print(b)
    a, b = b, a+b

def 피보나치(숫자):
    if 숫자 == 0 or 숫자 == 1:
        return 1
    return 피보나치(숫자-1) + 피보나치(숫자-2)

print(피보나치(5))


피보나치(5) -> 피보나치(4) + 피보나치(3)  ==> 5 + 3
피보나치(4) -> 피보나치(3) + 피보나치(2)  ==> 3 + 2
피보나치(3) -> 피보나치(2) + 피보나치(1)  ==> 2 + 1
피보나치(2) -> 피보나치(1) + 피보나치(0)  ==> 1 + 1


                     f(5)
                   /     \ 
                  4       3 
                 / \     / \ 
                3   2   2  1
               / \ / \  /\ 
              2  1 1 0 1 0


f(3) is called twice
f(2) is called 3 times


"""