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

def sum_of_1_to_n(n):
    return int((n+1)*(n/2))



if __name__ == '__main__':
    print(sum(8))
    print(find_biggest([1,52,3,4,5], 5))
    print(sum_of_1_to_n(8))