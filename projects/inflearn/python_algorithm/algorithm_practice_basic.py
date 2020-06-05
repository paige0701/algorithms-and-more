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


if __name__ == '__main__':

    one = One()
    print(one.find_kth_divisor_2(6, 5))
