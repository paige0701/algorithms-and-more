def cross_the_river(durability, dogs):
    result = [i['이름'] for i in dogs]

    for i in dogs:

        location = 0

        while location < len(durability)-1:
            location += int(i['점프력'])
            durability[location-1] -= int(i['몸무게'])
            if durability[location-1] < 0:
                result[result.index(i['이름'])] = 'fail'
                break
    return [i for i in result if i != 'fail']


if __name__ == '__main__':
    durability = [1, 2, 1, 4]

    dogs = [
        {
            '이름': '루비독',
            '나이': '95년생',
            '점프력': 3,
            '몸무게': 4
        },
        {
            '이름': '피치독',
            '나이': '95년생',
            '점프력': 3,
            '몸무게': 3
        },
        {
            '이름': '씨-독',
            '나이': '72년생',
            '점프력': 2,
            '몸무게': 1
        },
        {
            '이름': '코블독',
            '나이': '59년생',
            '점프력': 1,
            '몸무게': 1
        }
    ]

    print(cross_the_river(durability, dogs))