"""
    Given an array nums with n objects colored red, white, or blue, sort them in-place so that
    objects of the same color are adjacent, with the colors in the order red, white, and blue.

    We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

    You must solve this problem without using the library's sort function.
"""


class Solution:
    def sortColors(self, nums: list[int]) -> list[int]:
        """
        Do not return anything, modify nums in-place instead.
        """
        ind = 0
        while ind < len(nums) - 1:
            min_ind = ind
            min_item = nums[ind]

            for search_ind in range(ind + 1, len(nums)):
                if nums[search_ind] < min_item:
                    min_item = nums[search_ind]
                    min_ind = search_ind

            nums[ind], nums[min_ind] = nums[min_ind], nums[ind]
            ind += 1
        return nums


if __name__ == "__main__":
    assert Solution().sortColors([2, 0, 2, 1, 1, 0]) == [0, 0, 1, 1, 2, 2]
    assert Solution().sortColors([2, 0, 1]) == [0, 1, 2]
