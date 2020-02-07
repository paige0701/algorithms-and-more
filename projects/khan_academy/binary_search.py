"""
-BINARY SEARCH-

*** in order to use binary search, list must be sorted ***

- HOW BINARY SEARCH WORKS ?

target_number = 7
a = [1,2,3,4,5,6,7,8]

find the middle index of a list

if middle index value of list is smaller than the number you are looking for,
than remove the array items before middle index

so middle index is 3, 7 is in a2
a1 = [1,2,3,4] a2 = [5,6,7,8]

so remove a1

a = [5,6,7,8]

find the middle index again
a1 = [5,6] a2 = [7,8]

number 7 is in a2 so remove a1 .. and so on



- RUNNING TIME OF BINARY SEARCH

O(log n)

"""

def search(arr, target_value):
    l = 0
    r = len(arr)-1

    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == target_value:
            return mid
        elif arr[mid] < target_value:
            l = mid+1
        elif arr[mid] > target_value:
            r = mid-1
    return -1


def search_recursive(li, target, low, high):

    if low > high:
        return False
    else :

        mid = (low+high)//2

        if li[mid] == target:
            return mid
        elif li[mid] > target:
           return search_recursive(li, target, low, mid-1)
        elif li[mid] < target:
            return search_recursive(li, target, mid+1, high)


if __name__ == '__main__':

    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
              41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

    print("found index at ",search(primes, 73))

    assert search(primes, 222) == -1

    print(search_recursive(primes, 13, 0, len(primes) - 1))


