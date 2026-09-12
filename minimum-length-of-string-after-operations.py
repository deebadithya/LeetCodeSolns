"""
minimum-length-of-string-after-operations.py
3223. Minimum Length of String After Operations
Solved
Medium
Topics
Companies
Hint
You are given a string s.

You can perform the following process on s any number of times:

Choose an index i in the string such that there is at least one character to the left of index i that is equal to s[i], and at least one character to the right that is also equal to s[i].
Delete the closest character to the left of index i that is equal to s[i].
Delete the closest character to the right of index i that is equal to s[i].
Return the minimum length of the final string s that you can achieve.

 
"""

class Solution:
    def minimumLength(self, s: str) -> int:
        counts = [0] * 26
        for ch in s:
            counts[ord(ch) - ord('a')] += 1
        del_count = 0
        for c in counts:
            if c % 2 == 1:
                del_count += c - 1
            elif c > 3:
                del_count += c - 2 
        return len(s) - del_count

