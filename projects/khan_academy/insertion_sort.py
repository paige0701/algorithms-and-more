"""
Time complexity of insertion sort :
worst case : O(n^2)
best case : O(n)

a = [2, 10, 8, 3, 5]

   ←↓
[2, 10, 8, 3, 5]

       ←↓
[2, 10, 8, 3, 5]

           ←↓
[2, 8, 10, 3, 5]

              ←↓
[2, 3, 8, 10, 5]


[2, 3, 5, 8, 10]

"""


def insertion_element_in_the_array(li, target):
    li.append(target)
    for i in range(len(li), 0, -1):
        if li[i-1] > target:
            li[i], li[i-1] = li[i-1], target
    return li


def insertion_sort(array):
    for i in range(1, len(array)):
        insert(array, i-1, array[i])
    return array


def insert(array, right_index, value):

    i = right_index
    while i >= 0 and value < array[i]:
        array[i+1] = array[i]
        i = i - 1
    array[i+1] = value


# another way to do insert sort
# but with extra memory
def insert_sort(array):
    result = []
    while array:
        insert_value = array.pop()
        index = get_index_of_index_value(result, insert_value)
        result.insert(index, insert_value)
    return result


def get_index_of_index_value(array, insert_value):

    for i in range(len(array)):
        if insert_value < array[i]:
            return i
    return len(array)


if __name__ == '__main__':
    a = [1,2,4,5,6]
    assert insertion_element_in_the_array(a,3) == [1, 2, 3, 4, 5, 6]

    arr = [10,8,2,1,3]
    # print(insertion_sort([10,8,2,1,3]))

    print(insert_sort(arr))