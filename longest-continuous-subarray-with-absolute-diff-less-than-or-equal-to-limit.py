"""
longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit.py

1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
Solved
Medium
Topics
Companies
Hint
Given an array of integers nums and an integer limit, return the size of the longest non-empty subarray such that the absolute difference between any two elements of this subarray is less than or equal to limit.

 
"""
import collections

def longestSubarray(self, nums, limit: int) -> int:
    decQ, incQ = collections.deque(), collections.deque()
    ans, left = 0, 0
    for right, num in enumerate(nums):
        while decQ and num > decQ[-1]:
            decQ.pop()
        decQ.append(num)
        while incQ and num < incQ[-1]:
            incQ.pop()
        incQ.append(num)
        while decQ[0] - incQ[0] > limit:
            if decQ[0] == nums[left]:
                decQ.popleft()
            if incQ[0] == nums[left]:
                incQ.popleft()
            left += 1
        ans = max(ans, right - left + 1)
    return ans