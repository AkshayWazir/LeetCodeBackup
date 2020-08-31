from math import inf


def max_profit(prices):
    buy1, buy2 = inf, inf
    sell1, sell2 = 0, 0
    for i in range(len(prices)):
        buy1 = min(buy1, prices[i])
        sell1 = max(sell1, prices[i] - buy1)
        buy2 = min(buy2, prices[i] - sell1)
        sell2 = max(sell2, prices[i] - buy2)
    return sell2
