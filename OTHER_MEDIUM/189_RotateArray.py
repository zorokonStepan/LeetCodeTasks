"""
    Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
"""


class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_copy = nums[:]
        for ind in range(len(nums)):
            insert_ind = ind + k
            if insert_ind >= len(nums):
                insert_ind -= len(nums) * (insert_ind // len(nums))
            nums[insert_ind] = nums_copy[ind]

        return nums


if __name__ == "__main__":
    assert Solution().rotate([1, 2, 3, 4, 5, 6, 7], 3) == [5, 6, 7, 1, 2, 3, 4]
    assert Solution().rotate([-1, -100, 3, 99], 2) == [3, 99, -1, -100]
