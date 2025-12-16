"""
    Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        values = []

        cur = head
        while cur:
            values.append(cur.val)
            cur = cur.next

        return values == values[::-1]
