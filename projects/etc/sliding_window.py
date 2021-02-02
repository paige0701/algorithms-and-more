import sys


def sum_of_sub_array(strs, k):

    i, j = 0, k-1
    total = -sys.maxsize
    while j < len(strs):
        temp_max = sum(strs[i:j+1])
        total = max(temp_max, total)
        i += 1
        j += 1
    print(total)


# how sliding window works
def max_sum_sub_array(strs, k):

    max_value = - sys.maxsize
    current_running_sum = 0

    for i, v in enumerate(strs):
        current_running_sum += v
        if i >= k -1:
            max_value = max(max_value, current_running_sum)
            current_running_sum -= strs[i - (k-1)]
    print(max_value)


if __name__ == '__main__':
    strs = [8, 2, 1, 3, 9, 6, 15, 1, 4]
    k = 3
    sum_of_sub_array(strs, k)
    max_sum_sub_array(strs, k)



