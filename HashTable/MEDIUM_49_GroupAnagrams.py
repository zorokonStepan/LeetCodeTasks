"""
    Given an array of strings strs, group the anagrams together.
    You can return the answer in any order.
"""


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = {}

        for _str in strs:
            tmp = "".join(sorted(list(_str)))
            if tmp in anagrams:
                anagrams[tmp].append(_str)
            else:
                anagrams[tmp] = [_str]

        return [value for key, value in anagrams.items()]
