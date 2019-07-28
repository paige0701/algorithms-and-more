"""
You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.
"""


class Solution:
    def next_greater_element(self, num1, num2):

        result = []
        for i in num1:

            l = 0
            is_found = False
            while len(num2) > l :
                if num2[l] > i:
                    result.append(num2.pop(l))
                    print('----')
                    print(num2)
                    print('@@@@')
                    print( l)
                    is_found = True
                    break
                l+=1


            if is_found is False:
                result.append(-1)

        return result

if __name__ == '__main__':
    a = Solution()
    print(a.next_greater_element([4,1,2],[1,3,4,2]))