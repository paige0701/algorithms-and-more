def make_weird_string(s):

    new_list = []
    result = ''
    # for x in s.split(" "):
    #     for y in range(len(x)):
    #         result += x[y].upper() if y%2 == 0 else x[y].lower()


    num = 0

    for i in s:
        if i != ' ':
            result += i.upper() if num % 2 == 0 else i.lower()
            num +=1
        else:
            num = 0
            result += ' '
    return result
def main():
    st = input('input string : \n')
    print(make_weird_string(st))

if __name__ == '__main__':
    main()
