"""
    Write a function to find the longest common prefix string amongst an array of strings.

    If there is no common prefix, return an empty string "".
"""


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        longest_common_prefix = ""

        if len(strs) == 0:
            return longest_common_prefix

        if len(strs) == 1:
            return strs[0]

        sorted_strs = sorted(strs, key=lambda x: len(x))

        for s in sorted_strs[1:]:
            common_prefix = ""
            if s.startswith(sorted_strs[0]):
                common_prefix = sorted_strs[0]
            else:
                for e1, e2 in zip(sorted_strs[0], s):
                    if e1 == e2:
                        common_prefix += e1
                    else:
                        break

            if common_prefix == "":
                return ""

            if longest_common_prefix == "" or len(common_prefix) < len(longest_common_prefix):
                longest_common_prefix = common_prefix

        return longest_common_prefix
