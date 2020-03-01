class Solution:
    def subtract_product_and_sum(self, n):
        product, sum = 1, 0
        for i in str(n):
            product *= int(i)
            sum += int(i)
        return product-sum

    def findNumbers(self, nums):
        return len([i for i in nums if len(str(i)) % 2 == 0])

if __name__ == '__main__':
    solution = Solution()
    print(solution.subtract_product_and_sum(4421))
    print(solution.findNumbers([12,345,2,6,7896]))