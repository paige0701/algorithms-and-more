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

    @staticmethod
    def solution2():
        import sys
        sys.stdin = open('stack_queue_hash_heap/two.txt')
        n = input()
        answer = 0
        sticks = 0
        rasor_to_zero = n.replace('()', '0')

        for i in rasor_to_zero:
            if i == '(':
                sticks += 1
            elif i == '0':
                answer += sticks
            else:
                sticks -= 1
                answer += 1

        return answer


class Three:


    @staticmethod
    def get_number_by_operand(op):
        res = {'-': 1, '+': 1, '*': 2, '/': 2}
        return res[op]

    @staticmethod
    def postfix_exp():
        import sys
        sys.stdin = open('stack_queue_hash_heap/three.txt')
        a = input()
        res = ''
        stack = []
        for x in a:  # 숫자
            if x.isdecimal():
                res += x
            else:  # 연산자

                if x == '(':
                    stack.append(x)
                elif x == '*' or x == '/':
                    while stack and (stack[-1] == '*' or stack[-1] == '/'):
                        res += stack.pop()
                    stack.append(x)

                elif x == '+' or x == '-':
                    while stack and stack[-1] != '(':
                        res += stack.pop()
                    stack.append(x)
                elif x == ')':
                    while stack and stack[-1] != '(':
                        res += stack.pop()
                    stack.pop()

        while stack:
            res += stack.pop()

        print(res)


class Four:

    @staticmethod
    def calculate(operator, num1, num2):
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        else:
            return num1//num2

    def solve_postfix_exp(self):
        import sys
        sys.stdin = open('stack_queue_hash_heap/four.txt')
        a = list(input())
        stack = []

        for i in a:
            if i.isdecimal():
                stack.append(int(i))
            else:
                b = stack.pop()
                a = stack.pop()
                r = self.calculate(i, a, b)
                stack.append(r)
        print(stack[0])


class Five:
    @staticmethod
    def save_princess():
        from collections import deque
        n = 8
        k = 3
        deq = deque([i for i in range(1, n+1)])

        print(deq)

        while len(deq) > 1:
            i = 0
            while i < k:
                if i == k-1:
                    deq.popleft()
                else:
                    deq.append(deq.popleft())
                i += 1
        print(deq)

    @staticmethod
    def solution():
        from collections import deque
        n = 8
        k = 3
        dq = list(range(1, n+1))
        dq = deque(dq)
        while dq:
            for _ in range(k-1):
                cur = dq.popleft()
                dq.append(cur)
            dq.popleft()
            if len(dq) == 1:
                break
        print(dq)


class Six:
    @staticmethod
    def solution():
        from collections import deque
        n, m = 5, 0
        d = [1, 1, 9, 1, 1, 1]
        d = [(i, v) for i, v in enumerate(d)]
        print(d)
        d = deque(d)
        res = 0
        while True:
            cur = d.popleft()
            if any(cur[1] < x[1] for x in d):
                d.append(cur)
            else:
                res += 1
                if cur[0] == m:
                    break
        print(res)


class Seven:

    def solution(self):
        m = 'AFC'
        s = ['AFFDCCFF', 'FGCDAB', 'CTSBDEA']

        for i in range(len(s)):
            q = []
            for j in s[i]:
                if j in m and j not in q:
                    q.append(j)
            if m == ''.join(q):
                print('yes')
            else:
                print('no')

    def solution2(self):
        from collections import deque
        need = 'AFC'
        s = ['AFFDCCFF', 'FGCDAB', 'CTSBDEA']
        for i in range(len(s)):
            dq = deque(need)
            for x in s[i]:
                if x in dq:
                    if x != dq.popleft():
                        print('no')
                        break
            else:
                if len(dq) == 0:
                    print('yes')
                else:
                    print('no')


class Eight:
    def solution(self):
        import sys
        from collections import deque
        sys.stdin = open('stack_queue_hash_heap/eight.txt')
        n = int(input())
        words = deque()
        used = []
        for i in range(n):
            words.append(input())

        for i in range(n-1):
            used.append(input())

        while words:
            p = words.popleft()
            if p not in used:
                print(p)
                break

    def solution2(self):
        import sys
        sys.stdin = open('stack_queue_hash_heap/eight.txt')
        n = int(input())
        p = dict()
        for i in range(n):
            word = input()
            p[word] = 1

        for i in range(n-1):
            word = input()
            p[word] = 0

        for key, val in p.items():
            if val == 1:
                print(key)
                break


class Nine:
    @staticmethod
    def anagram():
        a = 'AbaAeCe'
        b = 'baeeACA'
        res = dict()
        for i in range(len(a)):
            if a[i] not in res:
                res[a[i]] = 1
            else:
                res[a[i]] += 1

            if b[i] in res:
                res[b[i]] -=1
            else:
                res[b[i]] = -1

        print(all(x == 0 for x in res.values()))

    @staticmethod
    def solution():
        a = 'AbaAeCe'
        b = 'baeeACA'
        str1 = dict()
        str2 = dict()

        for x in a:
            str1[x] = str1.get(x, 0) + 1  # dictionary 에서 str1[x]가 없어면 0을 넣고 아니면 +1
        for x in b:
            str2[x] = str2.get(x, 0) + 1

        for i in str1.keys():
            if i in str2.keys():
                if str1[i] != str2[i]:
                    print('No')
                    break
            else:
                print('No')
                break
        else:
            print('Yes')


class Ten:

    @staticmethod
    def min_heap():
        import sys
        import heapq as hq
        sys.stdin = open('stack_queue_hash_heap/ten.txt')
        a = []
        while True:
            n = int(input())
            if n == -1:
                break
            if n == 0:
                if len(a) == 0:
                    print(-1)
                else:
                    print(hq.heappop(a))

            else:
                hq.heappush(a, n)

        print(hq)


if __name__ == '__main__':
    one = One()
    # one.get_biggest_number_using_stack()

    two = Two()
    # two.solution()

    three = Three()
    # three.postfix_exp()

    four = Four()
    # four.solve_postfix_exp()

    five = Five()
    # five.solution()

    six = Six()
    # six.solution()

    seven = Seven()
    # seven.solution2()

    eight = Eight()
    # eight.solution2()

    nine = Nine()
    # nine.solution()

    ten = Ten()
    ten.min_heap()