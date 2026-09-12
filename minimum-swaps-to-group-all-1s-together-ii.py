"""
minimum-swaps-to-group-all-1s-together-ii.py
2134. Minimum Swaps to Group All 1's Together II
Solved
Medium
Topics
Companies
Hint
A swap is defined as taking two distinct positions in an array and swapping the values in them.

A circular array is defined as an array where we consider the first element and the last element to be adjacent.

Given a binary circular array nums, return the minimum number of swaps required to group all 1's present in the array together at any location.

"""
from typing import List
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        total_ones = sum(nums)
        
        # Edge cases
        if total_ones == 0 or total_ones == n:
            return 0
        
        current_ones = sum(nums[:total_ones])
        max_ones = current_ones
    
        for i in range(n):
            current_ones -= nums[i]
            current_ones += nums[(i + total_ones) % n]
            max_ones = max(max_ones, current_ones)
        
        return total_ones - max_ones