"""
    Given the head of a linked list, rotate the list to the right by k places.
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head

        len_linked_list = 0
        current = head

        while current:
            len_linked_list += 1
            current = current.next

        shift = k - (k // len_linked_list) * len_linked_list

        if shift == 0 or len_linked_list == 1:
            return head

        old_head = head
        current = head
        cnt = 1
        while cnt != len_linked_list - shift:
            current = current.next
            cnt += 1

        new_head = current.next
        current.next = None

        current = new_head

        while _next := current.next:
            current = _next

        current.next = old_head

        return new_head
