"""
binary-tree-inorder-traversal.py
94. Binary Tree Inorder Traversal
Solved
Easy
Topics
Companies
Given the root of a binary tree, return the inorder traversal of its nodes' values.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional, List
class Solution:
   
    def inorderTraversal(self, root: Optional[TreeNode], data=[]) -> List[int]:
        result = []
        self._inorder(root, result)
        return result

    def _inorder(self, node: Optional[TreeNode], result: List[int]):
        if node:
            self._inorder(node.left, result)
            result.append(node.val)
            self._inorder(node.right, result)
        