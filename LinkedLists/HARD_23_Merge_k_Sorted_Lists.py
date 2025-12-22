"""
    You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

    Merge all the linked-lists into one sorted linked-list and return it.
"""
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy_head = ListNode()
        current = dummy_head

        while any(lists):
            values = [(ind, item.val) for (ind, item) in enumerate(lists) if item]
            min_item = min(values, key=lambda x: x[1])
            min_node = lists[min_item[0]]
            current.next = min_node
            current = current.next

            lists[min_item[0]] = lists[min_item[0]].next

        return dummy_head.next
