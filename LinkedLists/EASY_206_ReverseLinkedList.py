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
        prev = ListNode(0)
        current_node = head
        while current_node:
            tmp = current_node.next
            current_node.next = prev.next
            prev.next = current_node
            current_node = tmp

        return prev.next

        # dummy = ListNode(0)
        # cur = head
        # while cur:
        #     tmp = cur.next
        #     cur.next = dummy.next
        #     dummy.next = cur
        #     cur = tmp

        # return dummy.next
