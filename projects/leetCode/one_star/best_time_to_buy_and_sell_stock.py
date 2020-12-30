import sys


def max_profit(prices):

    min_price = sys.maxsize
    profit = 0

    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price-min_price)
    return profit


if __name__ == "__main__":
    print(max_profit([7, 1, 5, 3, 6, 4]))
