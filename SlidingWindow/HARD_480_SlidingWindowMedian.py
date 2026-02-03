"""
    The median is the middle value in an ordered integer list.
    If the size of the list is even, there is no middle value.
    So the median is the mean of the two middle values.

    For examples, if arr = [2,3,4], the median is 3.
    For examples, if arr = [1,2,3,4], the median is (2 + 3) / 2 = 2.5.
    You are given an integer array nums and an integer k.
    There is a sliding window of size k which is moving from the very left
    of the array to the very right.
    You can only see the k numbers in the window.
    Each time the sliding window moves right by one position.

    Return the median array for each window in the original array.
    Answers within 10-5 of the actual value will be accepted.
"""


class Solution:
    def medianSlidingWindow(self, nums: list[int], k: int) -> list[float]:
        result = []
        calculate_median = self.even_median if k % 2 == 0 else self.not_even_median

        for ind in range(len(nums) - k + 1):
            result.append(calculate_median(nums[ind: ind + k]))

        return result

    def even_median(self, part: list[int]) -> float:
        part = sorted(part)
        return ((part[len(part) // 2 - 1]) + (part[len(part) // 2])) / 2

    def not_even_median(self, part: list[int]) -> float:
        part = sorted(part)
        return float(part[len(part) // 2])


if __name__ == "__main__":
    assert Solution().medianSlidingWindow([2147483647, 2147483647], 2) == [2147483647.00000]
    assert Solution().medianSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3) == [
        1.00000,
        -1.00000,
        -1.00000,
        3.00000,
        5.00000,
        6.00000,
    ]
    assert Solution().medianSlidingWindow([1, 2, 3, 4, 2, 3, 1, 4, 2], 3) == [
        2.00000,
        3.00000,
        3.00000,
        3.00000,
        2.00000,
        3.00000,
        2.00000,
    ]
