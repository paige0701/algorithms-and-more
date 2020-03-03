class Solution:
    def replaceElements(self, arr):
        result = []
        """
        이런 문재는 대부분 위에서 부터 룹을 돈다.
        """
        mx = -1
        for i in range(len(arr)-1, -1, -1):
            arr[i], mx = mx, max(arr[i], mx)
        return arr

if __name__ == "__main__":
    solution = Solution()
    print(solution.replaceElements([17,18,5,4,6,1]))