import math

def find_sqrt(s):

    # you can also use s ** 1/2 to find square root. instead of math.sqrt

    sqroot = int(math.sqrt(s))
    num = sqroot ** 2
    if num == s:
        return int((sqroot+1)**2)
    else :
        return -1





def main():
    a = int(input("Input a num \n"))
    print('answer = {}'.format(find_sqrt(a)))

if __name__ == '__main__':
    main()
