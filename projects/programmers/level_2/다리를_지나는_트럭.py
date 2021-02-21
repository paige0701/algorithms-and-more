def test(trucks, weight, length):

    time = 0
    bridge = [0] * length

    while bridge:

        time += 1
        bridge.pop(0)

        if trucks:

            if trucks[0] + sum(bridge) <= weight:
                bridge.append(trucks.pop(0))
            else:
                bridge.append(0)
    return time


if __name__ == '__main__':
    assert 8 == test([7, 4, 5, 6], 10, 2)
    assert 110 == test([10,10,10,10,10,10,10,10,10,10], 100, 100)
    assert 101 == test([10], 100, 100)