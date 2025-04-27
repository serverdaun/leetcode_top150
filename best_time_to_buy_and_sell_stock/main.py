from typing import List


def maxProfit(prices: List[int]) -> int:
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price

    return max_profit
    

prices = [2, 4, 1]
profit = maxProfit(prices=prices)
print(profit)