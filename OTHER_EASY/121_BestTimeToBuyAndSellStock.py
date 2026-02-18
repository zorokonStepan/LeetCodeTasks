"""
    You are given an array prices where prices[i] is the price of a given stock on the ith day.

    You want to maximize your profit by choosing a single day to buy one stock and choosing a
    different day in the future to sell that stock.

    Return the maximum profit you can achieve from this transaction.
    If you cannot achieve any profit, return 0.
"""


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy = prices[0]
        maxp = 0
        for i in range(len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            else:
                maxp = max(maxp, prices[i] - buy)
        return maxp


if __name__ == "__main__":
    assert Solution().maxProfit([7, 1, 5, 3, 6, 4, 0]) == 5
