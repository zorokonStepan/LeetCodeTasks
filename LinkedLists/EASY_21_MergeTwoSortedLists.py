"""
    You are given the heads of two sorted linked lists list1 and list2.

    Merge the two lists into one sorted list. The list should be made by splicing together
    the nodes of the first two lists.

    Return the head of the merged linked list.
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if list1 and list2:
            if list1.val <= list2.val:
                new_list_head = list1
                list1 = list1.next
            else:
                new_list_head = list2
                list2 = list2.next

            new_list_node = new_list_head

            while list1 and list2:
                if list1.val <= list2.val:
                    new_list_node.next = list1
                    new_list_node = new_list_node.next
                    list1 = list1.next
                else:
                    new_list_node.next = list2
                    new_list_node = new_list_node.next
                    list2 = list2.next

            new_list_node.next = list1 or list2
            return new_list_head
        elif list1:
            return list1
        elif list2:
            return list2
        else:
            return None
