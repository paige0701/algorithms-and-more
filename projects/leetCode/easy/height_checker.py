from copy import deepcopy

class Solution:


    def height_checker(self, heights):

        cloned_height = deepcopy(heights) # this is slowest
        cloned_height = heights[:] # this is faster than deep copy
        cloned_height = sorted(heights) # this is fastest !

        count = 0

        for i in range(len(heights)):
            if heights[i] != cloned_height[i]:
                count +=1

        return count

if __name__ == '__main__':
    sol = Solution()
    print(sol.height_checker([1,1,4,2,1,3]))

