"""
    Given the head of a singly linked list, reverse the list, and return the reversed list.
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        cur = head

        _next = None
        next_cur = cur.next
        cur.next = _next

        while next_cur:
            _next = cur
            cur = next_cur
            next_cur = cur.next
            cur.next = _next

        return cur
