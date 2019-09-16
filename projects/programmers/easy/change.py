# greedy algorithm


def min_num_of_change(change):

    coins = [500, 100, 50, 10]
    idx = 0
    result = []
    while change != 0:
        if coins[idx] <= change:
            change = change - coins[idx]
            result.append(coins[idx])
        else:
            idx = idx + 1
    return len(result)


if __name__ == '__main__':
    # count = count_substring(string, sub_string)
    print(min_num_of_change(170))
