def find_gcm(a,b):
    if a % b != 0:
        a, b = b, a % b
        find_gcm(a,b)
    else:
        print(b)

def find_lcm(a,b):
    return ''

def main():
    a = 192
    b = 72
    find_gcm(a, b)


if __name__ == '__main__':
    main()

# 이걸 람다로 풀 수 있을것이다 ! 이걸 해보자 ..
