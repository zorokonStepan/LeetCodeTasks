"""
    You are given the head of a singly linked-list. The list can be represented as:

    L0 → L1 → … → Ln - 1 → Ln
    Reorder the list to be on the following form:

    L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
    You may not modify the values in the list's nodes. Only nodes themselves may be changed.
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        nodes = []

        current = head
        while current:
            nodes.append(current)
            current = current.next

        first = nodes[:]
        second = nodes[::-1]
        second = second[: (len(nodes) // 2)]

        if len(nodes) % 2 == 0:
            first = first[: (len(nodes) // 2)]
            first.append(None)
        else:
            first = first[: (len(nodes) // 2) + 1]

        f_ind, s_ind = 0, 1
        while f_ind <= len(first) and s_ind <= len(second):
            first[f_ind].next = second[f_ind]
            second[f_ind].next = first[s_ind]
            f_ind += 1
            s_ind += 1

        if len(nodes) % 2 != 0:
            first[-1].next = None


if __name__ == "__main__":
    l4 = ListNode(5, None)
    l3 = ListNode(4, l4)
    l2 = ListNode(3, l3)
    l1 = ListNode(2, l2)
    head = ListNode(1, l1)

    # l3 = ListNode(4, None)
    # l2 = ListNode(3, l3)
    # l1 = ListNode(2, l2)
    # head = ListNode(1, l1)

    Solution().reorderList(head)
