import collections

def one_is_unique(string):
    print(len(string) == len(set(string)))

def two_check_permutation(str1, str2):
    print(sorted(str1) == sorted(str2))

def three_urlify(str1):
    str1 = str1.rstrip()
    print(str1.replace(' ', '%20'))

def four_palindrome_permutations(str1):
    str1 = str1.replace(' ', '')
    num = 0
    for i in collections.Counter(str1).values():
        print(i)
        if i % 2 != 0:
            num +=1

    return not num > 1

class FiveOneWay:

    def five_one_way(self, str1, str2):
        if len(str1) == len(str2):
            return self.one_edit_replace(str1, str2)
        elif len(str1) + 1 == len(str2):
            return self.one_edit_insert(str1, str2)
        elif len(str1) -1 == len(str2):
            return self.one_edit_insert(str2, str1)
        return False

    def one_edit_replace(self, s1, s2):
        edited = False
        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                if edited:
                    return False
                edited = True
        return True


    def one_edit_insert(self, s1, s2):
        edited = False
        i = j = 0
        while i < len(s1) and j < len(s2):
            if s1[i] != s2[j]:
                if edited:
                    return False
                edited = True
                j+=1
            else:
                i+=1
                j+=1
        return True

if __name__ == '__main__':
    # one_is_unique('abcc')
    # two_check_permutation('abc','ccc')
    # three_urlify('Mr John Smith     ')
    # print(four_palindrome_permutations('tact coa'))
    f = FiveOneWay()
    print(f.five_one_way('pale', 'ple'))