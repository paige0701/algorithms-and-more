def iterate_example(a,b):
    result = 0
    for i in range(len(a)):
        result += abs(a[i]-b[i])
    return result

def recursive(a, b, size):

    # base case
    if size == 0:
        return 0
    else:
        last = abs(a[size-1]-b[size-1])
        return recursive(a,b,size-1) + last

if __name__ == '__main__':

    # get total of difference in values in array in same index
    a = [2, 5, 10, 4, 56]
    b = [3, 4, 2, 11, 40]

    print(iterate_example(a,b))
    print(recursive(a,b,len(a)))