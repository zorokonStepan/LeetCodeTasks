"""
    Given the head of a linked list and an integer val, remove all the nodes of the
    linked list that has Node.val == val, and return the new head.
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head

        new_head = None
        current = head
        while new_head is None and current:
            if current.val != val:
                new_head = current
            else:
                current = current.next

        current = head
        _prev = current
        while current:
            if current.val == val:
                _prev.next = current.next
            else:
                _prev = current
            current = current.next

        return new_head
