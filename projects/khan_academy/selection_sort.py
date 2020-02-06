def swap(li, first, second):
    li[first], li[second] = li[second], li[first]

def find_min_index(li, start_index):


    min_value = li[start_index]
    min_index = start_index

    for i in range(start_index, len(li)):
        if li[i] < min_value:
            min_value = li[i]
            min_index = i
    return min_index


def selection_sort(li):

    for i in range(len(li)):
        min_index = find_min_index(li, i)
        swap(li, i, min_index)
    return li


if __name__ == '__main__':
    sorted = selection_sort([2,4,5,44,22,10])
    assert sorted == [2,4,5,10,22,44]

