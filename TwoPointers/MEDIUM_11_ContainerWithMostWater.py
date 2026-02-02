"""
    You are given an integer array height of length n.
    There are n vertical lines drawn such that the two endpoints
    of the ith line are (i, 0) and (i, height[i]).

    Find two lines that together with the x-axis form a container,
    such that the container contains the most water.

    Return the maximum amount of water a container can store.

    Notice that you may not slant the container.
"""


class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_amount = 0
        for step in range(1, len(height)):
            max_step_amount = 0
            for ind in range(len(height) - step):
                min_height = min(height[ind], height[ind + step])
                amount = min_height * step
                if amount > max_step_amount:
                    max_step_amount = amount

            if max_step_amount > max_amount:
                max_amount = max_step_amount

        return max_amount


if __name__ == "__main__":
    assert Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
