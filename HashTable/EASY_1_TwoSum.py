"""
    Given an array of integers nums and an integer target,
    return indices of the two numbers such that they add up to target.

    You may assume that each input would have exactly one solution,
    and you may not use the same element twice.

    You can return the answer in any order.
"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        set_nums = set(nums)
        for ind1, num1 in enumerate(nums):
            target_num = target - num1

            if target_num not in set_nums:
                continue
            else:
                for ind2, num2 in enumerate(nums):
                    if num2 == target_num and ind2 != ind1:
                        return [ind1, ind2]
