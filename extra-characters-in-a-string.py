"""
extra-characters-in-a-string.py
2707. Extra Characters in a String
Solved
Medium
Topics
Companies
Hint
You are given a 0-indexed string s and a dictionary of words dictionary. You have to break s into one or more non-overlapping substrings such that each substring is present in dictionary. There may be some extra characters in s which are not present in any of the substrings.
Return the minimum number of extra characters left over if you break up s optimally.
"""
from typing import List
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        wordSet = set(dictionary)
        n = len(s)
        
        # dp[i] will store the minimum extra characters in the substring s[i:]
        dp = [0] * (n + 1)
        
        # Fill dp array from right to left
        for i in range(n - 1, -1, -1):
            # By default, we assume the current character is extra
            dp[i] = dp[i + 1] + 1
            
            # Try to match any word from dictionary starting at index i
            for length in range(1, n - i + 1):
                if s[i:i + length] in wordSet:
                    dp[i] = min(dp[i], dp[i + length])
        
        return dp[0]