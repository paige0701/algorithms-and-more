class One:
    @staticmethod
    def get_biggest_number_using_stack():
        import sys
        sys.stdin = open('stack_queue_hash_heap/one.txt')
        n, m = map(int, input().split())
        num = list(map(int, str(n)))

        stack = []
        for x in num:
            while stack and m > 0 and stack[-1] < x:
                stack.pop()
                m -= 1
            stack.append(x)

        if m!=0:
            stack = stack[:-m]
        print(stack)


if __name__ == '__main__':
    one = One()
    one.get_biggest_number_using_stack()