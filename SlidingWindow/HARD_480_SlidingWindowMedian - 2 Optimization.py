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
from typing import Optional


class Solution:
    def medianSlidingWindow(self, nums: list[int], k: int) -> list[float]:
        result = []
        calculate_median = self._even_median if k % 2 == 0 else self._not_even_median

        window = sorted(nums[:k])
        result.append(calculate_median(window))

        for ind in range(1, len(nums) - k + 1):
            window = self._create_window(
                window=window, delete_item=nums[ind - 1], insert_item=nums[ind - 1 + k]
            )
            result.append(calculate_median(window))

        return result

    def _even_median(self, window: list[int]) -> float:
        return ((window[len(window) // 2 - 1]) + (window[len(window) // 2])) / 2

    def _not_even_median(self, window: list[int]) -> float:
        return float(window[len(window) // 2])

    def _create_window(self, window: list[int], delete_item: int, insert_item: int) -> list[int]:
        window = self._delete_item(window, delete_item)
        return self._insert_item(window, insert_item)

    def _delete_item(self, window: list[int], delete_item: int) -> list[int]:
        delete_ind = self._binary_search(window, delete_item)
        return window[:delete_ind] + window[delete_ind + 1 :]

    def _binary_search(self, window: list[int], target: int) -> Optional[int]:
        left = 0
        right = len(window) - 1

        current = (left + right) // 2

        while left <= right:
            if window[current] == target:
                return current
            if window[current] > target:
                right = current - 1
            else:
                left = current + 1

            current = (left + right) // 2

    def _insert_item(self, window: list[int], insert_item: int) -> list[int]:
        insert_ind = self._binary_search_insert(window, insert_item)
        return window[:insert_ind] + [insert_item] + window[insert_ind:]

    def _binary_search_insert(self, window: list[int], target: int) -> Optional[int]:
        left = 0
        right = len(window) - 1

        current = (left + right) // 2

        while left <= right:
            if window[current] == target:
                return current
            if window[current] > target:
                right = current - 1
            else:
                left = current + 1

            current = (left + right) // 2

        return left


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

    assert Solution()._binary_search([-1, 1, 3], -1) == 0
    assert Solution()._binary_search([-1, 1, 3], 1) == 1
    assert Solution()._binary_search([-1, 1, 3], 3) == 2
    assert Solution()._binary_search([-1, 1, 3], 8) is None

    assert Solution()._delete_item([-1, 1, 3], -1) == [1, 3]
    assert Solution()._delete_item([-1, 1, 3], 1) == [-1, 3]
    assert Solution()._delete_item([-1, 1, 3], 3) == [-1, 1]

    assert Solution()._binary_search_insert([-1, 1, 3], -1) == 0
    assert Solution()._binary_search_insert([-1, 1, 3], 1) == 1
    assert Solution()._binary_search_insert([-1, 1, 3], 3) == 2
    assert Solution()._binary_search_insert([-1, 1, 3], -5) == 0
    assert Solution()._binary_search_insert([-1, 1, 3], 5) == 3
    assert Solution()._binary_search_insert([-1, 1, 3], 0) == 1

    assert Solution()._insert_item([-1, 1, 3], -1) == [-1, -1, 1, 3]
    assert Solution()._insert_item([-1, 1, 3], 1) == [-1, 1, 1, 3]
    assert Solution()._insert_item([-1, 1, 3], 3) == [-1, 1, 3, 3]
    assert Solution()._insert_item([-1, 1, 3], -5) == [-5, -1, 1, 3]
    assert Solution()._insert_item([-1, 1, 3], 5) == [-1, 1, 3, 5]
    assert Solution()._insert_item([-1, 1, 3], 0) == [-1, 0, 1, 3]

    assert Solution()._create_window([-1, 1, 3], 1, -3) == [-3, -1, 3]
    assert Solution()._create_window([-3, -1, 3], 3, 5) == [-3, -1, 5]
    assert Solution()._create_window([-3, -1, 5], -1, 3) == [-3, 3, 5]
    assert Solution()._create_window([-3, 3, 5], -3, 6) == [3, 5, 6]
    assert Solution()._create_window([3, 5, 6], 5, 7) == [3, 6, 7]
