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


if __name__ == '__main__':

    one = One()

    for i in one.get_list():
        one.is_palindrome3(i)
