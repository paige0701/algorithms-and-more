def return_element_divisible_with_divisor(array, divisor):
    # result = list(filter(lambda x: x % divisor == 0, array))
    # result.sort()
    # return result if not result == [] else -1

    # 굳이 람다를 쓸 필요는 없음 그냥 한번 써보고 싶었다 ㅋㅋ
    result = [x for x in array if x % divisor == 0]
    result.sort()
    return result if not result == [] else [-1]

def main():
    print(return_element_divisible_with_divisor([2, 36, 1, 3],1))

if __name__ == '__main__':
    main()

