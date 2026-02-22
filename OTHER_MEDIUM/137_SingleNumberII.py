"""
    Given an integer array nums where every element appears three times except for one,
    which appears exactly once. Find the single element and return it.

    You must implement a solution with a linear runtime complexity and use only
    constant extra space.
"""


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        single_numbers = []
        numbers = set()
        for num in nums:
            if num in numbers:
                if num in single_numbers:
                    single_numbers.remove(num)
            else:
                single_numbers.append(num)
                numbers.add(num)
        return single_numbers[0]
