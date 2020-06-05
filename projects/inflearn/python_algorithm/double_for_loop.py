"""
*
**
***
****
*****
"""
def print_triangle():
    for i in range(5):
        for j in range(i+1):
            print('*', sep='', end=' ')
        print()


"""
*****
****
***
**
*
"""
def print_upside_down_triangle():
    n = 5
    for i in range(n):
        for j in range(n-i):
            print('*', end=' ')
        print()


if __name__ == '__main__':
    print_triangle()
    print_upside_down_triangle()