def insertion_sort(a):

    result = []
    while len(a) != 0:
        temp = a.pop(0)

        # result is empty
        if len(result) == 0:
            result.append(temp)
        else:
            idx = len(result)
            for i in range(0, len(result)):
                if temp < result[i]:
                    idx = i
                    break
            result.insert(idx, temp)
    return result


def insertion_sort2(list):
    for index in range(1, len(list)):
        value = list[index]
        i = index-1
        while i >= 0:
            if value < list[i]:
                list[i+1] = list[i]
                list[i] = value
                i-=1
            else:
                break

    return list

if __name__ == '__main__':
    print(insertion_sort([2,4,5,1,3]))
    print(insertion_sort2([2, 4, 5, 1, 3]))