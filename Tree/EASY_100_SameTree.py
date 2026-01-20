"""
    Given the roots of two binary trees p and q, write a function to check if they are the same
    or not.

    Two binary trees are considered the same if they are structurally identical,
    and the nodes have the same value.
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_queue = [p]
        q_queue = [q]

        while p_queue and q_queue:
            p, q = p_queue.pop(), q_queue.pop()

            if p and q:
                if p.val != q.val:
                    return False
                else:
                    p_queue = [p.left, p.right] + p_queue
                    q_queue = [q.left, q.right] + q_queue
            elif p or q:
                return False

        return True
