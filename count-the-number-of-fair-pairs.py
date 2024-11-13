"""
count-the-number-of-fair-pairs.py
2563. Count the Number of Fair Pairs
Solved
Medium
Topics
Companies
Hint
Given a 0-indexed integer array nums of size n and two integers lower and upper, return the number of fair pairs.

A pair (i, j) is fair if:

0 <= i < j < n, and
lower <= nums[i] + nums[j] <= upper
"""

from bisect import bisect_left, bisect_right

class Solution:
    def countFairPairs(self, v, lower, upper):
        v.sort()
        ans = 0
        for i in range(len(v) - 1):
            low = bisect_left(v, lower - v[i], i + 1)
            up = bisect_right(v, upper - v[i], i + 1)
            ans += up - low
        return ans