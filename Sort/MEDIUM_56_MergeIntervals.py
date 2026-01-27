"""
    Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping
    intervals, and return an array of the non-overlapping intervals that cover all the
    intervals in the input.
"""


class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        need_merge = True
        intervals = sorted(intervals, key=lambda x: x[0])

        while need_merge:
            for ind in range(len(intervals) - 1):
                if (intervals[ind][0] == intervals[ind + 1][0]) or (
                    intervals[ind][-1] >= intervals[ind + 1][0]
                ):
                    intervals[ind + 1] = [
                        intervals[ind][0],
                        max(intervals[ind][-1], intervals[ind + 1][1]),
                    ]
                    intervals.pop(ind)
                    break
            else:
                need_merge = False

        return intervals


if __name__ == "__main__":
    assert Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert Solution().merge([[1, 4], [2, 3]]) == [[1, 4]]
