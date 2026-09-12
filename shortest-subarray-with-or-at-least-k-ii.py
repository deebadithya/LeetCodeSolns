"""
shortest-subarray-with-or-at-least-k-ii.py
"""
from typing import List
inf = float('inf')
class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        suffix = {} # len(suffix) <= log(max(nums))
        # For 32-bit numbers, the hash map can only have at most 32 values.

        # Proof: suppose o[i] is the OR value of nums[:i + 1], 
        # then o[i + 1] is either equal to o[i] or have at least 1 more set bit than o[i]. 
        # Thus there can only be at most 32 unique values in o[0], o[1], ..., o[n]

        ans = inf

        for r, x in enumerate(nums):
            # new suffcies now end at nums[r]
            suffix = {val | x: l for val, l in suffix.items()}
            suffix[x] = r
            
            for val, l in suffix.items():
                if val >= k:
                    ans = min(ans, r - l + 1)
        
        if ans == inf:
            return -1
        return ans
