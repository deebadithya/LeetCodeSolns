"""
balanced-binary-tree.py
110. Balanced Binary Tree
Easy
Topics
Companies
Given a binary tree, determine if it is 
height-balanced
.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root):
        return self.Height(root) >= 0
    def Height(self, root):
        if root is None:
            return 0
        lh, rh = self.Height(root.left), self.Height(root.right)
        if lh < 0 or rh < 0 or abs( lh - rh ) > 1:
            return -1
        return max(lh, rh) + 1
