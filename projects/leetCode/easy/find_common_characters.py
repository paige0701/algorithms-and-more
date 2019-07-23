class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """

        longest_str = max(A, key=len)
        index = A.index(longest_str)
        duplicates = list()

        A.pop(index)
        for i in list(longest_str):
            num = 0
            temp = []
            while num < len(A):
                try:
                    curr = list(A[num])
                    found_index = curr.index(i)
                    if found_index > -1:
                        temp.append(curr.pop(found_index))
                        A[num] = ''.join(curr)
                except ValueError:
                    break
                num = num + 1
            if len(temp) == len(A):
                duplicates.append(i)
        return sorted(duplicates)

if __name__ == '__main__':
    a = Solution()
    print(a.commonChars(["bella","label","roller"]))