def print_su_bak(s):
    su = '수박'
    remainder = '수'

    if s % 2 == 0:
        return su * (s//2)
    else:
        return (su * (s // 2)) +remainder


    # 이렇게 하길 의도했을듯 ..
    # arr = su * s
    # return arr[:s]
def main():
    a = int(input("Input a number \n"))
    print('answer = {}'.format(print_su_bak(a)))

if __name__ == '__main__':
    main()



# 2 -> 수박
# 3 -> 수박수
# 4 -> 수박수박

a = 4//2


