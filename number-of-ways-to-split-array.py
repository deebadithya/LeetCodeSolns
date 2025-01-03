"""
number-of-ways-to-split-array.py
2270. Number of Ways to Split Array
Solved
Medium
Topics
Companies
Hint
You are given a 0-indexed integer array nums of length n.

nums contains a valid split at index i if the following are true:

The sum of the first i + 1 elements is greater than or equal to the sum of the last n - i - 1 elements.
There is at least one element to the right of i. That is, 0 <= i < n - 1.
Return the number of valid splits in nums.
"""
from typing import List
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        split_count = 0
        nums_len = len(nums)
        sums_ls = [0] * (nums_len + 1)
        for i in range(nums_len):
            sums_ls[i+1] = sums_ls[i] + nums[i]
        for i in range(1, nums_len):
            if sums_ls[i] >= ( sums_ls[nums_len] - sums_ls[i] ) :
                split_count += 1

        return split_count