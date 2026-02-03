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
        if len(height) < 2:
            return 0

        max_line, second_max_line = self.max_lines(height)
        max_amount = 0
        for step in range(len(height) - 1, 0, -1):
            possible_maximum = second_max_line * step
            if possible_maximum <= max_amount:
                break

            max_height = 0
            for ind in range(len(height) - step):
                min_height = min(height[ind], height[ind + step])
                if min_height > max_height:
                    max_height = min_height

            tmp = max_height * step
            if tmp > max_amount:
                max_amount = tmp

        return max_amount

    def max_lines(self, height: list[int]) -> tuple[int, int]:
        max_line, second_max_line = height[0], None

        for item in height[1:]:
            if item >= max_line:
                second_max_line = max_line
                max_line = item
            else:
                if second_max_line is None or item > second_max_line:
                    second_max_line = item

        return max_line, second_max_line


if __name__ == "__main__":
    assert Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert Solution().maxArea([1, 2, 3, 1000, 9]) == 9
