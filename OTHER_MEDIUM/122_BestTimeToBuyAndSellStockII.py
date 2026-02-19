"""
    You are given an integer array prices where prices[i] is the price of a given stock on the
    i**th day.

    On each day, you may decide to buy and/or sell the stock.
    You can only hold at most one share of the stock at any time.
    However, you can sell and buy the stock multiple times on the same day,
    ensuring you never hold more than one share of the stock.

    Find and return the maximum profit you can achieve.
"""


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy = prices[0]
        maxp = 0
        sum_maxp = 0

        for i in range(len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            else:
                sum_maxp += max(maxp, prices[i] - buy)
                buy = prices[i]
        return sum_maxp
