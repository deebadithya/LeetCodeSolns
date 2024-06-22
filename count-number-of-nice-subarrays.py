"""
count-number-of-nice-subarrays.py

1248. Count Number of Nice Subarrays
Solved
Medium
Topics
Companies
Hint
Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.
"""

class Solution:
    def numberOfSubarrays(self, nums, k: int) -> int:
        for i in range(len(nums)):
            nums[i] %= 2
        
        prefix_count = [0] * (len(nums) + 1)
        prefix_count[0] = 1
        s = 0
        ans = 0
        
        for num in nums:
            s += num
            if s >= k:
                ans += prefix_count[s - k]
            prefix_count[s] += 1
        
        return ans
        

        