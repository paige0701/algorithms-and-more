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

"""

def merge_sort(arr):
    if len(arr) > 1:

        mid = len(arr)//2

        low_half = arr[:mid]
        high_half = arr[mid:]

        merge_sort(low_half)
        merge_sort(high_half)


        i = j = k  = 0

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



if __name__ == '__main__' :
    a = [38, 27, 43, 3, 9, 82, 10]
    print(merge_sort(a))