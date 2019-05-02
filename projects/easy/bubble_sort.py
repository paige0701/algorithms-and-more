def swap(a,i,j):
    a[i], a[j] = a[j], a[i]

def bubble_sort():
    print('Bubble sort')
    a = [10,4,2,1,5]
    for i in range(len(a)-1):
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                swap(a, j, j+1)

    print(a)



def main():
    bubble_sort()


if __name__ == '__main__':
    main()