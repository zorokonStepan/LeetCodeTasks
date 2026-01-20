"""
    Given the root of a binary tree, check whether it is a mirror of itself
    (i.e., symmetric around its center).
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        p = root.left
        q = root.right

        if p is None and q is None:
            return True
        if p is None or q is None:
            return False

        p_queue = [p]
        q_queue = [q]

        while p_queue and q_queue:
            p = p_queue.pop()
            q = q_queue.pop()

            if p is None and q is None:
                continue
            elif p and q:
                if p.val != q.val:
                    return False
                else:
                    p_queue = [p.left, p.right] + p_queue
                    q_queue = [q.right, q.left] + q_queue
            else:
                return False

        return True
