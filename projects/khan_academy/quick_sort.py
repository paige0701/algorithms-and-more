"""
How Quick sort works

Time complexity - O(nLogn) - average case running time
O(n^2) - worst case scenario

** most sorting done in reality are Quick SORT Algorithm !

                          ↓
a = [7, 2, 1, 6, 8, 5, 3, 4]
Choose the rightmost element for pivot

After partitioning
              ↓
a = [2, 1, 3, 4, 8, 5, 7, 6]
         ↙️     ↘️
           ↓            ↓
    [2, 1, 3] [8, 5, 7, 6]
    ↙️️
    [1, 2]
        ↘
        [2] -> one element? stop the recursion


Quicksort(A, start, end)
{
    if (start < end) {

        pIndex = partition(A, start, end) -> will rearrange the array and returns the pivot
        QuickSort(A, start, pIndex-1)
        QuickSort(A, pIndex +1, end)

    }

}

Qs(A, 0, 7)
Qs(A, 0, 2)
Qs(A, 0, 1)
Qs(A, 0, -1) -> invalid
Qs(A, 1, 1) -> invalid
Qs(A, 3, 2) -> Invalid
Qs(A, 4, 7)
Qs(A, 4, 4) -> Invalid
Qs(A, 6, 7)
etc

Partitioning logic

pivot -> A[end]
pIndex -> start

pIndex                   pivot
     ↓                    ↓
a = [7, 2, 1, 6, 8, 5, 3, 4]


for i from start to end-1
    if A[i] <= pivot:
        swap(A[i], A[pIndex])
        pIndex +1
swap(pIndex, pivot)

pIndex  i                  pivot
     ↓  ↓                  ↓
a = [7, 2, 1, 6, 8, 5, 3, 4]
i(i) is smaller than pivot(4) so swap 7 and 2
swap pIndex and i

   pIndex  i               Pivot
        ↓  ↓              ↓
a = [2, 7, 1, 6, 8, 5, 3, 4]

i(1) is smaller than pivot(4) so swap 7 and 1

      pIndex  i           Pivot
           ↓  ↓            ↓
a = [2, 1, 7, 6, 8, 5, 3, 4]


i(6) is bigger than pivot(4) so just increment i

      pIndex     i        Pivot
           ↓     ↓         ↓
a = [2, 1, 7, 6, 8, 5, 3, 4]


i(8) is bigger than pivot(4) so just increment i

      pIndex        i     Pivot
           ↓        ↓      ↓
a = [2, 1, 7, 6, 8, 5, 3, 4]


i(5) is bigger than pivot(4) so just increment i

      pIndex           i  Pivot
           ↓           ↓  ↓
a = [2, 1, 7, 6, 8, 5, 3, 4]


since i(3) is smaller than pivot(4)
swap pIndex and i

        pIndex         i  Pivot
              ↓        ↓  ↓
a = [2, 1, 3, 6, 8, 5, 7, 4]


swap pIndex and pivot

            PIVOT
              ↓
a = [2, 1, 3, 4, 8, 5, 7, 6]



"""
def quick_sort(array, start, end):
    if start < end:
        pivot = partition(array, start, end)
        quick_sort(array, start, pivot-1)
        quick_sort(array, (pivot + 1) , end)
    return array

def partition(array, start, end):

    pivot = array[end]
    i = start

    for j in range(start, end):
        if array[j] <= pivot:
            array[i], array[j] = array[j], array[i]
            i = i + 1


    array[i], array[end] = array[end], array[i]
    return i



if __name__ == '__main__':
    arr = [5,10,3,1,7, 9]
    assert quick_sort(arr, 0, len(arr)-1) == [1, 3, 5, 7, 9, 10]