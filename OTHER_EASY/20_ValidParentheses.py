"""
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
    determine if the input string is valid.

    An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_parentheses = {"(", "{", "["}
        match_parentheses = {")": "(", "}": "{", "]": "["}

        for item in s:
            if item in open_parentheses:
                stack.append(item)
            else:
                if not stack or match_parentheses[item] != stack.pop():
                    return False

        if stack:
            return False
        return True
