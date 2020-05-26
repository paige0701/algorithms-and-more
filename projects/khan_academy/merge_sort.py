"""
how  merge sort works?

        [14, 7, 3, 12,  9, 11, 6, 2]
                ↙️         ↘️               recursively divide in to half
    [14, 7, 3, 12]         [9, 11, 6, 2]
        ↙️   ↘️                ↙️   ↘️      recursively divide in to half
    [14, 7] [3, 12]        [9, 11] [6, 2]
      ↙️↘️   ↙️↘️            ↙️↘️   ↙️↘️    recursively divide in to half
    14  7    3  12          9  11  6  2     this is the base case. when divided in to half, only one element is left
     ↘️        ↙️            ↘️     ↙️      merge
    [7, 14]  [3, 12]      [9, 11] [2, 6]
      ↘️        ↙️         ↘️        ↙️     merge
      [3, 7, 12, 14]       [2, 6, 9, 11]
                ↘️          ↙️              merge
         [2, 3, 6, 7, 9, 11, 12, 14]


how to merge actually work?

 i       j
 ↓       ↓
[7, 14] [3, 12]

compare i and j find smaller number

[3]


increment j since j was smaller than i

 i           j
 ↓           ↓
[7, 14] [3, 12]

compare i and j get smaller number

[3, 7]

increment i since i was smaller than j
    i        j
    ↓        ↓
[7, 14] [3, 12]

compare i and j get smaller number
[3, 7, 12, 14]



Running time of merge sort algorithm is O(n Log 2 n)
it is important to note that merge sort does not sort in place
It needs an extra space for storing temporary low half and high half

"""


# merge sort using pointer!
def merge_sort(arr):
    if len(arr) > 1:

        mid = len(arr)//2

        low_half = arr[:mid]
        high_half = arr[mid:]

        merge_sort(low_half)
        merge_sort(high_half)

        i = j = k = 0

        while i < len(low_half) and j < len(high_half):
            if low_half[i] < high_half[j]:
                arr[k] = low_half[i]
                i += 1
            else:
                arr[k] = high_half[j]
                j += 1
            k += 1

        while i < len(low_half):
            arr[k] = low_half[i]
            i += 1
            k += 1

        while j < len(high_half):
            arr[k] = high_half[j]
            j += 1
            k += 1

        return arr


def merge_sort_different_way(arr):

    result = []
    mid = len(arr)//2

    if len(arr) <= 1:
        return arr

    first_half = merge_sort_different_way(arr[:mid])
    second_half = merge_sort_different_way(arr[mid:])

    while first_half and second_half:

        if first_half[0] < second_half[0]:
            result.append(first_half.pop(0))
        else:
            result.append(second_half.pop(0))

    while first_half:
        result.append(first_half.pop(0))

    while second_half:
        result.append(second_half.pop(0))

    return result


if __name__ == '__main__':
    a = [38, 27, 43, 3, 9, 82, 10]
    print(merge_sort(a))
    print(merge_sort_different_way(a))