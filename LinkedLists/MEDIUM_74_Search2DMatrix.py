"""
    You are given an m x n integer matrix matrix with the following two properties:

    Each row is sorted in non-decreasing order.
    The first integer of each row is greater than the last integer of the previous row.
    Given an integer target, return true if target is in matrix or false otherwise.

    You must write a solution in O(log(m * n)) time complexity.
"""
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # search row
        min_row_index = 0 - 1
        max_row_index = len(matrix) + 1

        current_row_index = (min_row_index + max_row_index) // 2

        while True:
            if matrix[current_row_index][0] <= target <= matrix[current_row_index][-1]:
                row_index = current_row_index
            else:
                if target < matrix[current_row_index][0]:
                    max_row_index = current_row_index
                else:
                    min_row_index = current_row_index

                prev_current_row_index = current_row_index
                current_row_index = (min_row_index + max_row_index) // 2

                if prev_current_row_index == current_row_index:
                    return False

        min_col_index = 0 - 1
        max_col_index = len(matrix[row_index]) + 1

        current_col_index = (min_col_index + max_col_index) // 2

        while True:
            if matrix[row_index][current_col_index] == target:
                return True

            if target < matrix[row_index][current_col_index]:
                max_col_index = current_col_index
            else:
                min_col_index = current_col_index

            prev_current_col_index = current_col_index
            current_col_index = (min_col_index + max_col_index) // 2

            if prev_current_col_index == current_col_index:
                return False


if __name__ == "__main__":
    assert (
        Solution().searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=3)
        is True
    )

    # assert Solution().searchMatrix(
    #     matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]],
    #     target = 13
    # ) == False
