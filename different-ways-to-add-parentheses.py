"""
different-ways-to-add-parentheses.py
241. Different Ways to Add Parentheses
Solved
Medium
Topics
Companies
Given a string expression of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. You may return the answer in any order.
The test cases are generated such that the output values fit in a 32-bit integer and the number of different results does not exceed 104.
"""
from typing import List

class Solution:
    def diffWaysToCompute(self, exp: str, memo = {}) -> List[int]:
        res = []
        if exp in memo: return memo[exp]
        for i in range(len(exp)):
            oper = exp[i]
            if oper == "+" or oper == "-" or oper == "*": 
                sub_str1 = self.diffWaysToCompute( exp[0 : i] )
                sub_str2 = self.diffWaysToCompute( exp[i + 1 : ] )
                for i in sub_str1:
                    for j in sub_str2:
                        if oper == "*":
                            res.append(int(i) * int(j))
                        if oper == "+":
                            res.append(int(i) + int(j))
                        if oper == "-":
                            res.append(int(i) - int(j))
        if len(res) == 0:
            res.append(int(exp))
        memo[exp] = res
        return res
    
# link : https://leetcode.com/problems/different-ways-to-add-parentheses/solutions/5811506/easy-efficient-solution-beats-93-5-users-iterative-memoization-python