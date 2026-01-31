"""
    Given an integer array nums and an integer k, return the k most frequent elements.
    You may return the answer in any order.
"""


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        numbers = {}
        for num in nums:
            if num in numbers:
                numbers[num] += 1
            else:
                numbers[num] = 1

        counts = {}
        for num, count in numbers.items():
            if count in counts:
                counts[count].append(num)
            else:
                counts[count] = [num]

        for count in counts.keys():
            counts[count] = sorted(counts[count])

        result = []
        for item in sorted(counts.items(), key=lambda x: x[0], reverse=True):
            result += item[1]

        return result[:k]
