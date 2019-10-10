"""
정렬 기초 #1 선택 정렬

1. 운동장에 a ~ g 까지 학생들이 서있다. 여기서 가장 키가 작은 사람을 뽑느다. "C"
[a,b,c,d,e,f,g] => [a,b,d,e,f,g]

==> [c]

2. [a,b,d,e,f,g] 여기서 제일 작은 사람을 찾는다. "A"
[a,b,d,e,f,g] => [b,d,e,f,g]
==> [c, a]

이런식으로 선택해서 뺴는 것?

trading smallest number

O(n^2)
1. [5,2,3,1,4]
2. [1,2,3,5,4]
3. [1,2,3,5,4]
4. [1,2,3,5,4]
5. [1,2,3,4,5]
"""


def selection_sort_asc(a):
    n = len(a)
    for i in range(0, n-1):
        min_idx = i # 0
        for j in range(i+1,n):
            if a[j] < a[min_idx]: #
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a

def selection_sort_desc(a):
    n = len(a)
    for i in range(0,n-1):
        max_idx = i
        for j in range(i+1, n):
            if a[j] > a[max_idx]:
                max_idx = j
        a[i], a[max_idx] = a[max_idx], a[i]
    return a


def basic_selection_sort(a):

    result = []
    while a:
        temp = find_min_val(a)
        val = a.pop(temp)
        result.append(val)
    return result



def find_min_val(a):

    n = len(a)
    idx = 0
    for i in range(1, n):
        if a[i] < a[idx]:
            idx = i

    return idx




if __name__ == '__main__':
    print(selection_sort_asc([2,4,5,1,3]))
    print(basic_selection_sort([2,4,5,1,3]))
    print(selection_sort_desc([2,4,5,1,3]))
