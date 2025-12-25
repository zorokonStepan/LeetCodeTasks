"""
    There is an integer array nums sorted in ascending order (with distinct values).

    Prior to being passed to your function, nums is possibly left rotated at an unknown
    index k (1 <= k < nums.length) such that the resulting array is
    [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
    For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].

    Given the array nums after the possible rotation and an integer target,
    return the index of target if it is in nums, or -1 if it is not in nums.

    You must write an algorithm with O(log n) runtime complexity.
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return 0 if target == nums[0] else -1

        min_value_index = 0
        prev_value = nums[0]

        for ind, value in enumerate(nums[1:]):
            if value < prev_value:
                min_value_index = ind + 1
                break
            prev_value = value

        if min_value_index == 0:
            target_nums = nums
            use_shift = False
        elif target <= nums[-1]:
            target_nums = nums[min_value_index:]
            use_shift = True
        else:
            target_nums = nums[:min_value_index]
            use_shift = False

        left = 0
        right = len(target_nums)
        current = (left + right) // 2

        while True:
            if target == target_nums[current]:
                if use_shift:
                    return current + min_value_index
                return current

            if target > target_nums[current]:
                left = current
            else:
                right = current

            prev = current
            current = (left + right) // 2

            if prev == current:
                return -1


if __name__ == "__main__":
    assert Solution().search([4, 5, 6, 7, 0, 1, 2], target=0) == 4
    assert Solution().search([1, 3], target=4) == -1
