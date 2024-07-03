"""
minimum-difference-between-largest-and-smallest-value-in-three-moves.py
1509. Minimum Difference Between Largest and Smallest Value in Three Moves
Solved
Medium
Topics
Companies
Hint
You are given an integer array nums.

In one move, you can choose one element of nums and change it to any value.

Return the minimum difference between the largest and smallest value of nums after performing at most three moves.

"""
from typing import List
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        nums.sort()
        ans = nums[-1] - nums[0]
        for i in range(4):
            ans = min(ans, nums[-(4 - i)] - nums[i] )
        return ans