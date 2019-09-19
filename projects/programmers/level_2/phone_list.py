def solution(phone_book):
    phone_book.sort(key=lambda x: len(str(x)))

    for i, val in enumerate(phone_book):
        for target in range(i + 1, len(phone_book)):
            if str(phone_book[target]).startswith(str(val)):
                return False
    return True

if __name__ == '__main__':
    print(solution([12, 222,203,11923]))