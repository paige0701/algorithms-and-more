def no_consecutive_nums(val):
    a = [y for idx,y in enumerate(val) if idx != 0 and val[idx-1] != val[idx]]
    a.insert(0,val[0])
    return a

def main():
    print(no_consecutive_nums([1,1,3,3,0,1,1]))

if __name__ == '__main__':
    main()

