class One:

    # K번째 약수 풀이
    # 두 개의 자연수 N과 K가 주어졌을 떄 N의 약수들 중 K 번째로 작은 수를 출력하라
    # K 번째로 작은 수가 없다면 -1를 리턴한다.
    @staticmethod
    def find_kth_divisor(n, k):

        result = []
        for i in range(1, n+1):
            if n % i == 0:
                result.append(i)
        return -1 if len(result) < k else result[k - 1]

    @staticmethod
    def find_kth_divisor_2(n, k):

        cnt = 0
        for i in range(1, n+1):
            if n % i == 0:
                cnt += 1
            if cnt == k:
                return i
        else:
            return -1


class Two:

    @staticmethod
    def find_kth_smallest_number():
        import sys
        sys.stdin = open('k_th_smallest_number.txt', 'rt')
        T = int(input())
        for i in range(T):
            n, s, e, k = map(int, input().split())
            li = list(map(int, input().split()))
            sorted_arr = sorted(li[s-1:e])
            print(i+1, sorted_arr[k-1])


class Three:

    @staticmethod
    def find_kth_biggest_number():

        """
        1부터 100사의의 자연수가 적힌 N장의 카드를 가지고 있고, 거기서 3장을 뽑아서
        그의 합을 기록하고 그것을 정렬해서 K번째 큰 값을 찾는 것이다..
        """

        import sys
        sys.stdin = open('kth_biggest_number.txt', 'rt')
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        s = set()  # set을 이용한 중복 제거
        for i in range(n):
            for j in range(i+1, n):
                for m in range(j+1, n):
                    s.add(a[i]+a[j]+a[m])
        res = list(s)
        res.sort(reverse=True)
        print(res[k-1])


class Four:

    @staticmethod
    def find_rep_value():

        import math
        a = [65, 73, 66, 87, 92, 67, 55, 79, 75, 80]
        ave = math.ceil(sum(a)/10)
        min = 2147000000
        score = 0
        result = 0
        for i, v in enumerate(a):
            tmp = abs(v-ave)
            if tmp < min:
                min = tmp
                score = v
                result = i + 1
            elif tmp == min:
                if v > score:
                    score = v
                    result = i+1
        print(ave, result)


class Five:

    @staticmethod
    def find_biggest_sum_from_two_dices():

        n, m = 4, 6
        d = {}

        for i in range(1, n+1):
            for j in range(1, m+1):

                if i+j not in d:
                    d[i+j] = 1
                else:
                    d[i+j] += 1

        m = max(d.items(), key=lambda x: x[1])[1]

        for i in d.items():
            if i[1] == m:
                print(i[0], end=' ')
        print()


class Six:

    @staticmethod
    def digit_sum(num):

        result = 0
        """
        for i in str(num):
            result += int(i)
        return result
        """

        # 자릿수 더하는 법!!!!!!!!!!!!!!!!!!
        # not changing number to string than int again
        while num > 0:
            result = num % 10
            num = num//10
        return result

    def get_biggest_number_from_digit_sum(self):
        import sys
        sys.stdin = open('digit_sum.txt', 'rt')
        n = input()
        li = list(map(int, input().split()))

        max = 0
        for i in li:
            tot = self.digit_sum(i)
            if tot > max:
                tot = max
                res = i

        """ How i did it !"""
        # print(n, li)
        # result = {}
        # for i in li:
        #     result[i] = self.digit_sum(i)
        # r = max(result.items(), key=lambda x: x[1])
        # return r[1]

        return res


if __name__ == '__main__':

    # one = One()
    # print(one.find_kth_divisor_2(6, 5))
    # two = Two()
    # two.find_kth_smallest_number()
    #
    # three = Three()
    # three.find_kth_biggest_number()

    # four = Four()
    # four.find_rep_value()

    five = Five()
    five.find_biggest_sum_from_two_dices()

    six = Six()
    print(six.get_biggest_number_from_digit_sum())