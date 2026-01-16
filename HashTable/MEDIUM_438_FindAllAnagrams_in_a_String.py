"""
    Given two strings s and p, return an array of all the start indices of p's anagrams in s.
    You may return the answer in any order.
"""


class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        n = len(p)
        template = "".join(sorted(list(p)))
        indx = []

        for i in range(len(s) - n + 1):
            if "".join(sorted(list(s[i: i + n]))) == template:
                indx.append(i)

        return indx
