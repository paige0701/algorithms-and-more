import collections
import numpy

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


def six_string_compression(s1):
    compressed = []
    counter = 0
    for i in range(len(s1)):
        if i !=0 and s1[i] != s1[i-1]:
            compressed.append(s1[i-1] + str(counter))
            counter = 0
        counter +=1
    compressed.append(s1[-1] + str(counter))
    return min(s1, ''.join(compressed), key=len)

def nine_string_rotation(s1, s2):
    return s2 in (s1*2)

def eight_zero_matrix(matrix):
    pass

def seven_rotate_matrix(arr):
    # arr = arr[::-1]
    # arr.reverse()
    # for i in range(len(arr)):
    #     for j in range(i):
    #         arr[j][i], arr[i][j] = arr[i][j], arr[j][i]

    return list(zip(*reversed(arr)))

if __name__ == '__main__':
    # one_is_unique('abcc')
    # two_check_permutation('abc','ccc')
    # three_urlify('Mr John Smith     ')
    # print(four_palindrome_permutations('tact coa'))
    # f = FiveOneWay()
    # print(f.five_one_way('pale', 'ple'))
    # print(six_string_compression('aaabbcc'))
    # print(nine_string_rotation('waterbottle', 'erbottler'))
    # print(eight_zero_matrix(3,3))
    print(seven_rotate_matrix([[1,2,3],[4,5,6],[7,8,9]]))