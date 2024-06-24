"""
minimum-number-of-k-consecutive-bit-flips.py

995. Minimum Number of K Consecutive Bit Flips
Solved
Hard
Topics
Companies
You are given a binary array nums and an integer k.

A k-bit flip is choosing a subarray of length k from nums and simultaneously changing every 0 in the subarray to 1, and every 1 in the subarray to 0.

Return the minimum number of k-bit flips required so that there is no 0 in the array. If it is not possible, return -1.

A subarray is a contiguous part of an array.

"""

class Solution:
    def minKBitFlips(self, nums, k: int) -> int:
        n = len(nums)
        flipped = 0
        res = 0
        isFlipped = [0] * n
        
        for i in range(n):
            if i >= k:
                flipped ^= isFlipped[i - k]
            if flipped == nums[i]:
                if i + k > n:
                    return -1
                isFlipped[i] = 1
                flipped ^= 1
                res += 1
        
        return res