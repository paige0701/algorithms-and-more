
def is_unique(l):
    l = list(l)
    l.sort()
    result = False
    # sort than check if adjacent value is same
    # for i, v in enumerate(l):
    #     if i != len(l)-1 and v == l[i+1]:
    #         result = True
    #         break


    # use hashmap to find duplicate
    map = {}
    for i,v in enumerate(l):
        if map.get(v) is None:
            map[v] = i
        else:
            result = True
            break

    return result

if __name__ == '__main__':
    # count = count_substring(string, sub_string)
    print(is_unique(list('asd')))