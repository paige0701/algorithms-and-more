def sum(num):
    if num == 0:
        return 0

    return sum(num-1)+ num

if __name__ == '__main__':
    print(sum(5))