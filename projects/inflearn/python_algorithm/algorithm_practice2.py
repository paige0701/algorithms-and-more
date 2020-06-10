class One:

    @staticmethod
    def get_list():
        import sys
        sys.stdin = open('is_palindrome.txt', 'rt')
        n = int(input())

        li = []
        for i in range(n):
            li.append(input())
        return li

    def is_palindrome(self, li):

        if len(li) == 0 or len(li) == 1:
            return 'yes'
        elif li[0].lower() != li[-1].lower():
            return 'No'
        else:
            return self.is_palindrome(li[1:-1])

    @staticmethod
    def is_palindrome3(s):
        s = s.lower()
        print(s == s[::-1])

    @staticmethod
    def is_palindrome2(s):

        s = s.lower()
        size = len(s)
        for i in range(size//2):

            if s[i] != s[-1-i]:
                print('No')
                break
        else:
            print('Yes')


class Two:

    @staticmethod
    def extract_only_numbers_and_print_its_divisors():

        import sys
        sys.stdin = open('extract_numbers.txt', 'rt')
        s = input()
        li = ''
        for i in s:
            try:
                s = int(i)
                li += str(s)
            except:
                pass
        print(int(li))

        cnt = 0
        for i in range(1, int(li)+1):
            if int(li) % i == 0:
               cnt += 1
        print(cnt)

    @staticmethod
    def solution():
        import sys
        sys.stdin = open('extract_numbers.txt', 'rt')
        s = input()
        res = 0
        for i in s:
            if i.isdecimal():
               res = res * 10 + int(i)

        print(res)
        cnt = 0
        for i in range(1, res+1):
            if res % i == 0:
                cnt +=1
        print(cnt)



if __name__ == '__main__':

    one = One()

    # for i in one.get_list():
    #     one.is_palindrome3(i)

    two = Two()
    two.solution()
