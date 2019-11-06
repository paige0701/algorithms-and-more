# find a peak if it exists
# one dimensional version
# straight forward algorithm

# a = [1, 2, '', 'n/2 -1', 'n/2', '', '', 'n-1', 'n'] # divide and conquer


def find_a_peak(list):
    n = len(list)
    print('len', n)

    print('middle', n//2)
    # look at n/2 position look to the right and look to the left
    if list[n // 2] < list[n // 2 - 1]:
        # only look at left half
        print(list[0:n//2])
        find_a_peak(list[0:n//2])


    elif list[n // 2] < list[n // 2 + 1]:
        # only look at right half
        find_a_peak(list[n // 2 + 1:n])

    else:
        # this is a peak
        return list[n//2]


def findPeakUtil(arr, low, high, n):
    # Find index of middle element
    # (low + high)/2
    mid = low + (high - low) / 2
    mid = int(mid)


    # Compare middle element with its
    # neighbours (if neighbours exist)


    if ((mid == 0 or arr[mid - 1] <= arr[mid]) and
        (mid == n - 1 or arr[mid + 1] <= arr[mid])):
        return mid

    # If middle element is not peak and
    # its left neighbour is greater
    # than it, then left half must
    # have a peak element
    elif (mid > 0 and arr[mid - 1] > arr[mid]):
        return findPeakUtil(arr, low, (mid - 1), n)

    # If middle element is not peak and
    # its right neighbour is greater
    # than it, then right half must
    # have a peak element
    else:
        return findPeakUtil(arr, (mid + 1), high, n)


# A wrapper over recursive
# function findPeakUtil()
def findPeak(arr, n):
    return findPeakUtil(arr, 0, n - 1, n)


if __name__ == '__main__':
    li = [1,2,3,3,5, 2,1,0]
    n = len(li)
    print(findPeak(li, n))



"""

Computation stand point -> execution of this algorithm
T(n)
work algorithm does on input of size n

T(n/2) + O(1)
theta one -> Two comparisons you do looking at left and right

base case = T(1) = O(1)
T(n) = O(1) ... + O(1) == log n times = O(log2n)

"""
#
#

