"""
    Given two sorted arrays nums1 and nums2 of size m and n respectively,
    return the median of the two sorted arrays.

    The overall run time complexity should be O(log (m+n)).
"""


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums3 = self._merge(nums1, nums2)
        if len(nums3) % 2 == 0:
            return (nums3[len(nums3) // 2 - 1] + nums3[len(nums3) // 2]) / 2
        else:
            return float(nums3[len(nums3) // 2])

    def _merge(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums3 = []
        ind_1, ind_2 = 0, 0

        while ind_1 < len(nums1) and ind_2 < len(nums2):
            if nums1[ind_1] <= nums2[ind_2]:
                nums3.append(nums1[ind_1])
                ind_1 += 1
            else:
                nums3.append(nums2[ind_2])
                ind_2 += 1

        if ind_1 == len(nums1):
            nums3 += nums2[ind_2:]
        else:
            nums3 += nums1[ind_1:]

        return nums3


if __name__ == "__main__":
    assert Solution().findMedianSortedArrays([1, 3], [2]) == float(2)
    assert Solution().findMedianSortedArrays([1, 2], [3, 4]) == float(2.5)
