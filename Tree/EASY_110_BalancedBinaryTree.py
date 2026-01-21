"""
    Given a binary tree, determine if it is height-balanced.

    A height-balanced binary tree is a binary tree in which the depth of the two subtrees
    of every node never differs by more than one.
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        queue = [root]
        while queue:
            tmp = []
            for node in queue:
                if self.is_balanced(node) is False:
                    return False
                if node:
                    tmp.append(node.left)
                    tmp.append(node.right)
            queue = tmp

        return True

    def is_balanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        p = root.left
        q = root.right

        hight_p = self.hight_tree(p)
        hight_q = self.hight_tree(q)

        if abs(hight_p - hight_q) > 1:
            return False
        return True

    def hight_tree(self, root: Optional[TreeNode]) -> int:
        hight = 0
        row = [root]
        while row:
            hight += 1
            tmp = []

            for node in row:
                if node:
                    tmp.append(node.left)
                    tmp.append(node.right)

            row = tmp

        return hight
