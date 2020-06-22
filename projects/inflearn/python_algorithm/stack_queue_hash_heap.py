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

        if m != 0:
            stack = stack[:-m]
        print(stack)


class Two:
    def find_metal_sticks(self):
        import sys
        sys.stdin = open('stack_queue_hash_heap/two.txt')
        n = input()
        stack =[n[1]]
        sum = 0
        for i in range(1, len(n)):

            if n[i] == ')' and n[i-1] == '(':
                stack.pop()
                sum += len(stack)
            elif n[i] == ')':
                stack.pop()
                sum += 1
            else:
                stack.append(n[i])
        print(sum)

    def solution(self):
        import sys
        sys.stdin = open('stack_queue_hash_heap/two.txt')
        n = input()
        stack = []
        total = 0
        for i in range(len(n)):
            if n[i] == '(':
                stack.append(n[i])
            else:
                stack.pop()
                if n[i-1] == '(':
                    total += len(stack)
                else:
                    total += 1
        print(total)


if __name__ == '__main__':
    one = One()
    # one.get_biggest_number_using_stack()

    two = Two()
    two.solution()