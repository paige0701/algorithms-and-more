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

if __name__ == '__main__':
    print(insertion_sort([2,4,5,1,3]))