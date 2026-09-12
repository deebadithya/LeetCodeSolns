"""
combination-sum.py
39. Combination Sum
Medium
Topics
Companies
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
frequency
 of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
"""
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if target == 0: return [[]]
        if target < 0: return None
        tot = []
        for ind, num in enumerate(candidates):
            ways = self.combinationSum(candidates[ind:], target-num)
            if ways != None:
                current_combs = [ [num] + i for i in ways ]
                tot.extend(current_combs)
        return tot
#https://leetcode.com/problems/combination-sum/solutions/5721560/simple-recursive-solution-easy-to-understand-9-line-code-python