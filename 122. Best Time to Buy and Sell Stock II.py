def max_profit(prices):
    i, valley, peak, max_prof = 0, prices[0], prices[0], 0
    while i < len(prices) - 1:
        while i < len(prices) - 1 and prices[i] >= prices[i + 1]:
            i += 1
        valley = prices[i]
        while i < len(prices) - 1 and prices[i] < prices[i + 1]:
            i += 1
        peak = prices[i]
        max_prof += peak - valley
    return max_prof


