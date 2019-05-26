def sumMatrix(A,B):
    answer = []
    for i in range(len(A)):
        tmp=[]
        for j in range(len(A[i])):
            tmp.append(A[i][j]+B[i][j])
        answer.append(tmp)
    return answer


def main():

    a = [[1,2],[2,3]]
    b = [[3,4],[5,6]]

    print(sumMatrix(a,b))


if __name__ == '__main__':
    main()
