"""
create-binary-tree-from-descriptions.py
2196. Create Binary Tree From Descriptions
Solved
Medium
Topics
Companies
Hint
You are given a 2D integer array descriptions where descriptions[i] = [parenti, childi, isLefti] indicates that parenti is the parent of childi in a binary tree of unique values. Furthermore,

If isLefti == 1, then childi is the left child of parenti.
If isLefti == 0, then childi is the right child of parenti.
Construct the binary tree described by descriptions and return its root.

The test cases will be generated such that the binary tree is valid.
"""
from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:  
        mp = {}
        parents = set()
        childrens = set()

        for x in descriptions:
            if x[0] in mp:
                mp[x[0]][x[2]] = x[1]
            else:
                arr = [None, None]
                arr[x[2]] = x[1]
                mp[x[0]] = arr
            
            parents.add(x[0])
            childrens.add(x[1])
        
        parent = None
        for p in parents:
            if p not in childrens:
                parent = p
                break
        parent_node = TreeNode(parent)
        def builder(node):
            children = mp.get(node.val)
            if not children:
                return
            if children[1]:
                node.left = TreeNode(children[1])
                builder(node.left)
            if children[0]:
                node.right = TreeNode(children[0])
                builder(node.right)
        builder(parent_node)
        return parent_node
        # if description[i][1] has any element parent means it already has child.


        