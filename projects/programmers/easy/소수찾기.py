def is_prime(num):

    for i in range(2, num+1):

        if num == 2 or num == 3:
            return True
        else:
            if num % i == 0:
                return False
            else:
                return True


        # if i%2 != 0 and i == num:
        #     answer =+ 1
        #     print(answer)
            # if len(list(filter(lambda x: (i % x == 0 and x != i), range(2, i + 1)))) == 0:
        #     answer+=1


def main():

  print(list(filter(lambda x : is_prime(x), range(2,10+1))))


if __name__ == '__main__':
    main()

