def find_second_largest_score():
    l = []
    scores = set()

    for _ in range(int(input())):
        name = input()
        score = float(input())
        l.append([name, score])
        scores.add(score)

    the_one = sorted(scores)[1]

    result = []

    for i in l:
        if i[1] == float(the_one):
            result.append(i[0])

    for i in sorted(result):
        print(i)

if __name__ == '__main__':
    find_second_largest_score()
