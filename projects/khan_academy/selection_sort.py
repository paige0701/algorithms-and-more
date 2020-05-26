"""
selection sort

 ↓  →
[2, 3 ,15 ,7 ,20 ,1]
from sub array == [3, 15, 7, 20, 1] find a smallest number
smallest number is 1 so swap 2 and 1

    ↓  →
[1, 3, 15, 7, 20, 2]
from sub array == [15, 7, 20, 2] find a smallest number
smallest number is 2 so swap 3 and 2

        ↓  →
[1, 2, 15, 7, 20, 3]
from sub array == [7, 20, 3] find a smallest number
smallest number is 3 so swap 15 and 3

          ↓   →
[1, 2, 3, 7, 20, 15] ....


looping through list = linear time
swapping = linear
finding min index = exponential

most significant is exponential

selection sort is O(n^2)

"""


def swap(arr, first, second):
    arr[first], arr[second] = arr[second], arr[first]


def find_min_index(arr, start_index):

    min_value = arr[start_index]
    min_index = start_index

    for i in range(start_index, len(arr)):
        if arr[i] < min_value:
            min_value = arr[i]
            min_index = i
    return min_index


def selection_sort(arr):

    for i in range(len(arr)):
        min_index = find_min_index(arr, i)
        swap(arr, i, min_index)
    return arr


# using 내장 함수
def 선택정렬(l):
    result = []
    while l:
        result.append(min(l))
        l.pop(l.index(min(l)))

    return result


if __name__ == '__main__':
    li = [2, 4, 5, 44, 22, 10]
    sorted_result = selection_sort(li)
    assert sorted_result == [2, 4, 5, 10, 22, 44]

    print(선택정렬(li))
