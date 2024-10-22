"""
kth-largest-sum-in-a-binary-tree.py
"""

# Definition for a binary tree node.
from typing import Optional
import list2tree
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1
        queue = deque([root])
        level_sums = []
        while queue:
            level_sum = 0
            level_len = len(queue)

            for _ in range(level_len):
                current = queue.popleft()
                level_sum += current.val

                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            level_sums.append(level_sum)
        
        if k <= len(level_sums):
            return sorted(level_sums, reverse = True)[k-1]
        else:
            return -1
                    
inp = list2tree.from_list([5,8,9,2,1,3,7,4,6])
soln = Solution()
result = soln.kthLargestLevelSum(inp, 5)    

print(result)
        