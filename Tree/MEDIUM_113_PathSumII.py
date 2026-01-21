"""
    Given the root of a binary tree and an integer targetSum, return all root-to-leaf
    paths where the sum of the node values in the path equals targetSum.
    Each path should be returned as a list of the node values, not node references.

    A root-to-leaf path is a path starting from the root and ending at any leaf node.
    A leaf is a node with no children.
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> list[list[int]]:
        if root is None:
            return []

        if root.left is None and root.right is None:
            if root.val == targetSum:
                return [[root.val]]
            else:
                return []

        paths = []
        self.path(root.left, [root.val], paths)
        self.path(root.right, [root.val], paths)

        valid_paths = [path for path in paths if sum(path) == targetSum and len(path) > 1]
        return valid_paths

    def path(self, node: Optional[TreeNode], prev: list[int], paths: list[list[int]]):
        if node is None:
            return

        if node.left is None and node.right is None:
            paths.append(prev + [node.val])
            return

        self.path(node.left, prev + [node.val], paths)
        self.path(node.right, prev + [node.val], paths)
