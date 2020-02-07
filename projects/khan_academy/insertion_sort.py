def insertion_sort(li, target):
    li.append(target)
    for i in range(len(li), 0, -1):
        if li[i-1] > target:
            li[i], li[i-1] = li[i-1], target
    return li


if __name__ == '__main__':
    a = [1,2,4,5,6]
    assert insertion_sort(a,3) == [1, 2, 3, 4, 5, 6]
