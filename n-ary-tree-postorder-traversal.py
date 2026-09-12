"""
n-ary-tree-postorder-traversal.py
590. N-ary Tree Postorder Traversal
Solved
Easy
Topics
Companies
Given the root of an n-ary tree, return the postorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)
"""


class Solution:
    def postorder(self, root):
        if root == None:
            return []

        res = []
        def dfs(root):
            for x in root.children:
                dfs(x)
            res.append(root.val)
        
        dfs(root)

        return res


        