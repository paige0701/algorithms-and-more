def sum_of_divisors(s):
    # result = 0
    # for i in range(1, s+1):
    #     if s%i == 0:
    #         result+=i
    # return result

    # 약수는 증간까지만 룹을 돌면 된다.
    # 12 일 경우 어짜피 12의 약수는 6까지 밖에 없다

    # this is such a clever code !
    return s + sum([i for i in range(1,(s//2)+1) if s%i == 0])





def main():
    a = int(input("Input a string \n"))
    print('answer = {}'.format(sum_of_divisors(a)))

if __name__ == '__main__':
    main()
