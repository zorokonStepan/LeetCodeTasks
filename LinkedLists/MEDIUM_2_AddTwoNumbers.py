"""
    You are given two non-empty linked lists representing two non-negative integers.
    The digits are stored in reverse order, and each of their nodes contains a single digit.
    Add the two numbers and return the sum as a linked list.

    You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        save_value = 0
        save_node = None
        head_new_list = None

        while l1 and l2:
            value = l1.val + l2.val + save_value
            save_value = value // 10
            value %= 10

            node = ListNode(val=value)
            if save_node:
                save_node.next = node
            save_node = node
            if head_new_list is None:
                head_new_list = node

            l1, l2 = l1.next, l2.next

        l3 = l1 or l2
        while l3:
            value = l3.val + save_value
            save_value = value // 10
            value %= 10

            node = ListNode(val=value)
            save_node.next = node
            save_node = node

            l3 = l3.next

        if save_value:
            node = ListNode(val=save_value)
            save_node.next = node

        return head_new_list
