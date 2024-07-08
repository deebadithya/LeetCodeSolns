"""
longest-substring-without-repeating-characters.py
3. Longest Substring Without Repeating Characters
Solved
Medium
Topics
Companies
Hint
Given a string s, find the length of the longest 
substring
 without repeating characters.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr = ""
        longest = 0
        for i in range(0, len(s)):
            if s[i] not in substr:
                substr += s[i]
            else:
                if len(substr) > longest:
                    longest = len(substr)
                substr = substr[substr.find(s[i]) + 1 : ] + s[i]     
        if len(substr) > longest:
            return len(substr)
        return longest

            
            
