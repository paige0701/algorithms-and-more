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

