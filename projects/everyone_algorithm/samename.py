def find_duplicate(li):
    n = len(li)

    result = set()
    for i in range(0,n-1):
        for j in range(i+1, n):
            if li[i] == li[j]:
               result.add(li[i])
    return result

def find_all_combinations(li):
    r = list(set(li))
    print(r)
    n = len(r)
    for i in range(0,n-1):
        for j in range(i+1, n):
            print(r[i] + ' - ' + r[j])




if __name__ == '__main__':
    print(find_duplicate(['paige', 'martin', 'james', 'paige']))
    find_all_combinations(['paige', 'martin', 'james', 'paige'])