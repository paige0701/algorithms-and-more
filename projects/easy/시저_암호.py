def caesar_cipher(s, n):

    result = ''
    for x in list(s):
        if x != ' ':
            code = ord(x) + n
            if x.isupper():
                if code > 90:
                    code = 90 - 26 + (code-90)
            else :
                if code > 122:
                    code = 122 - 26 + (code-122)
            result += chr(code)
        else :
            result += x

    return result

def main():
    st = input('input string : \n')
    num = int(input('input a number : \n'))
    print(caesar_cipher(st, num))

if __name__ == '__main__':
    main()
