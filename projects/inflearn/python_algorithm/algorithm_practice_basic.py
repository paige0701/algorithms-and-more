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


if __name__ == '__main__':

    one = One()
    # print(one.find_kth_divisor_2(6, 5))
    two = Two()
    two.find_kth_smallest_number()

    three = Three()
    three.find_kth_biggest_number()
