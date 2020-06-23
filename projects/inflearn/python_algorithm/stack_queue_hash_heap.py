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


if __name__ == '__main__':
    one = One()
    # one.get_biggest_number_using_stack()

    two = Two()
    # two.solution()

    three = Three()
    # three.postfix_exp()

    four = Four()
    four.solve_postfix_exp()