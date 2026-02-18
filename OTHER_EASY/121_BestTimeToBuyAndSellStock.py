"""
    You are given an array prices where prices[i] is the price of a given stock on the ith day.

    You want to maximize your profit by choosing a single day to buy one stock and choosing a
    different day in the future to sell that stock.

    Return the maximum profit you can achieve from this transaction.
    If you cannot achieve any profit, return 0.
"""


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        prices = self._del_last_zeros(prices)

        min_value = min(prices)
        max_value = max(prices)

        min_index = prices.index(min_value)
        max_index = len(prices) - 1 - prices[::-1].index(max_value)
        if min_index < max_index:
            return max_value - min_value

        max_profit = 0
        for ind in range(len(prices) - 1):
            tmp = max(prices[ind + 1 :]) - prices[ind]
            if tmp > 0:
                if max_profit < tmp:
                    max_profit = tmp
        return max_profit

    def _del_last_zeros(self, prices: list[int]) -> list[int]:
        if prices[-1] == 0:
            count = 1
            current = prices[-count]
            while current == 0:
                count += 1
                current = prices[-count]

            prices = prices[: len(prices) - count + 1]
            if not prices:
                return [0, 0]
        return prices


if __name__ == "__main__":
    assert Solution().maxProfit([7, 1, 5, 3, 6, 4, 0]) == 5
