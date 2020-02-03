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



if __name__ == '__main__':

    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
              41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

    print("found index at ",search(primes, 73))
    assert search(primes, 222) == -1
