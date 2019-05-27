def find_gcm(a,b):

    if a > b:
        a,b = b,a

    for x in range(a, 0, -1) :
        if a%x == 0 and b%x == 0:
            return x

def find_lcm(a,b):

    if a > b:
        a,b = b,a

    for x in range(b, a*b+1, b):
        if x % a == 0:
            return x


def main():
    a = 72
    b = 192
    print(find_lcm(a,b))
    print(find_gcm(a, b))




if __name__ == '__main__':
    main()

# 이걸 람다로 풀 수 있을것이다 ! 이걸 해보자 ..
