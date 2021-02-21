def test():
    progresses = [95, 90, 99, 99, 80, 99]
    speeds = [1, 1, 1, 1, 1, 1]

    comb = list(zip(progresses, speeds))
    import collections

    results = collections.deque()
    target = 100

    for i in comb:
        p = i[0]
        s = i[1]

        remainder = target - p

        import math
        r = math.ceil(remainder / s)
        results.append(r)

    count = 0
    res = []
    upper = results[0]

    while results:

        if results[0] <= upper:
            count += 1
            results.popleft()
        else:
            upper = results[0]
            res.append(count)
            count = 0
    res.append(count)

    print(res)


if __name__ == '__main__':

    test()