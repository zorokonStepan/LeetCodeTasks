from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        current = (left + right) // 2

        while left <= right:
            if nums[current] == target:
                return current

            if nums[current] > target:
                right = current - 1
            else:
                left = current + 1

            current = (left + right) // 2

        return -1


if __name__ == "__main__":
    assert Solution().search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert Solution().search([-1, 0, 3, 5, 9, 12], 2) == -1
    assert Solution().search([2, 5], 5) == 1
    assert Solution().search([2, 5], 2) == 0
