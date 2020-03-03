"""
Characters ('a' to 'i') are represented by ('1' to '9') respectively.
Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.
"""
class Solution:
    def freqAlphabets(self, s):
        i, result = len(s)-1, []
        while i >= 0:
            if s[i] == '#':
                result.append(chr(int((s[i-2] + s[i-1])) + 96))
                i-=3
            else:
                result.append(chr(int(s[i]) + 96))
                i-=1

        return ''.join(result[::-1])



if __name__ == '__main__':
    s = Solution()
    print(s.freqAlphabets('10#11#12'))
