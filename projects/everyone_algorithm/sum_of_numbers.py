def sum(num):
    if num == 0:
        return 0

    return sum(num-1)+ num


def fact(num):
    if num == 1:
        return 1
    return num * fact(num-1)


def find_biggest(li, num):
    if num == 1:
        return li[0]

    max = find_biggest(li, num-1)
    if max > li[num-1]:
        return max
    else:
        return li[num-1]



if __name__ == '__main__':
    print(sum(5))
    print(find_biggest([1,52,3,4,5], 5))