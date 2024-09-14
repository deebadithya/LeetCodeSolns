"""
longest-subarray-with-maximum-bitwise-and.py
"""
from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_val = max(nums)
        prev = 0
        counts = 1
        longest_len = 1
        for num in nums:
            if num == max_val and prev == max_val:
                counts+=1
                longest_len = max(longest_len, counts)
            else:
                counts = 1
            prev = num
        return longest_len