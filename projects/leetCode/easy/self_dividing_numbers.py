def self_dividing_numbers(left, right):
    result = []
    for i in range(left, right + 1):
        if 0 < i < 10:
            result.append(i)
        else:
            strigifiedNum = str(i)
            isSelfDividing = True
            num = 0
            while num < len(strigifiedNum):
                n = int(strigifiedNum[num])
                num += 1
                if n == 0:
                    isSelfDividing = False
                    break
                if i % n != 0:
                    isSelfDividing = False
                    break
            if isSelfDividing:
                result.append(i)
    return result


if __name__ == '__main__':
    print(self_dividing_numbers(1,22))
