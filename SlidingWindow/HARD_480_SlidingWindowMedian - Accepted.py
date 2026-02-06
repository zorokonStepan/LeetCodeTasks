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

    ---

    To calculate the median, we can maintain divide array into subarray equally: small and large. All elements in small are no larger than any element in large. So median would be (largest in small + smallest in large) / 2 if small's size = large's size. If large's size = small's size + 1, median is smallest in large.

    Thus, we can use heap here to maintain small(max heap) and large(min heap) so we can fetch smallest and largest element in logarithmic time.

    We can also maintain "large's size - small's size <= 1" and "smallest in large >= largest in small" by heap's property: once large's size - small's size > 1, we pop one element from large and add it to small. And vice versa when small's size > large's size.

    Besides, since its a sliding window median, we need to keep track of window ends. So we will also push element's index to the heap. So each element takes a form of (val, index). Since Python's heapq is a min heap, so we convert small to a max heap by pushing (-val, index).

    Intially for first k elements, we push them all into small and then pop k/2 element from small and add them to large.
    Then we can intialize our answer array as [large[0][0] if k & 1 else (large[0][0]-small[0][0])/2] as we discussed above.

    Then for rest iterations, each time we add a new element x whose index is i+k, and remove an old element nums[i] which is out of window scope. Then we calculate our median in current window as the same way before.
    If right end's x is no smaller than large[0], then it belongs to large heap. If left end's nums[i] is no larger than large[0], then it belongs to small heap. So we will add one to large while remove one from small and heaps' sizes will be unbalanced. So we will move large[0] to small to rebalance two heaps.
    Vice versa when we have to add one to small while remove one from large.

    But we don't have to hurry and remove element in each iteration. As long as nums[i] is neither small[0] nor large[0], it has no effect to median calculation. So we wait later and use a while loop to remove those out-of-window small[0] or large[0] at one time. This also make whole logic clearer.

    Since we are using k-size heap here, the time complexity is O(nlogk) and space complexity is O(logk).

    https://leetcode.com/problems/sliding-window-median/solutions/262689/python-small-large-heaps/
"""
import heapq


class Solution:
    def medianSlidingWindow(self, nums: list[int], k: int) -> list[float]:
        small, large = [], []
        for i, x in enumerate(nums[:k]):
            heapq.heappush(small, (-x, i))
        for _ in range(k - (k >> 1)):
            self.move(small, large)
        ans = [self.get_med(small, large, k)]
        for i, x in enumerate(nums[k:]):
            if x >= large[0][0]:
                heapq.heappush(large, (x, i + k))
                if nums[i] <= large[0][0]:
                    self.move(large, small)
            else:
                heapq.heappush(small, (-x, i + k))
                if nums[i] >= large[0][0]:
                    self.move(small, large)
            while small and small[0][1] <= i:
                heapq.heappop(small)
            while large and large[0][1] <= i:
                heapq.heappop(large)
            ans.append(self.get_med(small, large, k))
        return ans

    def move(self, h1, h2):
        x, i = heapq.heappop(h1)
        heapq.heappush(h2, (-x, i))

    def get_med(self, h1, h2, k):
        return h2[0][0] * 1. if k & 1 else (h2[0][0] - h1[0][0]) / 2


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
