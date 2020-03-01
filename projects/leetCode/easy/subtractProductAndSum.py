from math import log


class Solution:
    def subtract_product_and_sum(self, n):
        product, sum = 1, 0
        for i in str(n):
            product *= int(i)
            sum += int(i)
        return product-sum

    def findNumbers(self, nums):

        """
        int(log(x, 10)) % 2) 어떤 숫자의 로그 베이스 10의 값을 찾고 소수점을 날린다. 이것의 % 값을 찾았을 떄
        x 의 digit 이 짝수일 경우 1을 리턴한다 1은 True라는 뜻!
        """
        sum(1 for x in nums if int(log(x, 10)) % 2)


        return len([i for i in nums if len(str(i)) % 2 == 0])

if __name__ == '__main__':
    solution = Solution()
    print(solution.subtract_product_and_sum(4421))
    print(solution.findNumbers([12,345,2,6,7896]))