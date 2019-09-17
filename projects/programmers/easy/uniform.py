def get_total(n, lost, reserve):

    if 1 < n < 30:
        safe_students = n - len(lost)

        # _r = [i for i in reserve if i not in lost]


        for i in reserve:
            if i in lost:
                reserve.remove(i)
                lost.remove(i)
                safe_students+=1

        for i in reserve:

            for index, value in enumerate(lost):
                if value - 1 == i or value + 1 == i or value == i:
                    lost.pop(index)
                    safe_students += 1
                    break
        return safe_students



def main():
    print(get_total(10,[2,3,4,5], [3,7]))

if __name__ == '__main__':
    main()

