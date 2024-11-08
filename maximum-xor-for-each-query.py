"""
maximum-xor-for-each-query.py
1829. Maximum XOR for Each Query
Solved
Medium
Topics
Companies
Hint
You are given a sorted array nums of n non-negative integers and an integer maximumBit. You want to perform the following query n times:

Find a non-negative integer k < 2maximumBit such that nums[0] XOR nums[1] XOR ... XOR nums[nums.length-1] XOR k is maximized. k is the answer to the ith query.
Remove the last element from the current array nums.
Return an array answer, where answer[i] is the answer to the ith query.
"""
from typing import List
class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        n = len(nums)
        xorr = nums[0]
        max_xor = (1 << maximumBit) - 1
        
        for i in range(1, n):
            xorr ^= nums[i]
        
        ans = []
        for i in range(n):
            ans.append(xorr ^ max_xor)
            xorr ^= nums[n - 1 - i]
        
        return ans

        