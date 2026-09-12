"""
unique-length-3-palindromic-subsequences.py
1930. Unique Length-3 Palindromic Subsequences
Solved
Medium
Topics
Companies
Hint
Given a string s, return the number of unique palindromes of length three that are a subsequence of s.

Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.

A palindrome is a string that reads the same forwards and backwards.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
"""
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        letters = set(s)
        ans = 0
        
        for letter in letters:
            i, j = s.index(letter), s.rindex(letter)
            between = set()
            
            for k in range(i + 1, j):
                between.add(s[k])
            
            ans += len(between)

        return ans