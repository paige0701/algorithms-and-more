import copy
def add(val, array):
    copied = copy.deepcopy(array)
    a = copied[val[0]-1:val[1]]
    a = sorted(a)
    print(a)
    return a[val[2]-1]

def kthNumbers(array, commands):
    a = []
    for i in commands:
        a.append(add(i, array))
    print(a)


def main():
    print(kthNumbers([1,5,2,6,3,7], [[2,5,3], [4,4,1], [1,7,3]]))

if __name__ == '__main__':
    main()

# 이걸 람다로 풀 수 있을것이다 ! 이걸 해보자 ..
