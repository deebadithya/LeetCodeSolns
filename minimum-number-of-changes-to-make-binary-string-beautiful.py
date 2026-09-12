"""
minimum-number-of-changes-to-make-binary-string-beautiful.py
2914. Minimum Number of Changes to Make Binary String Beautiful
Solved
Medium
Topics
Companies
Hint
You are given a 0-indexed binary string s having an even length.

A string is beautiful if it's possible to partition it into one or more substrings such that:

Each substring has an even length.
Each substring contains only 1's or only 0's.
You can change any character in s to 0 or 1.

Return the minimum number of changes required to make the string s beautiful.
"""

class Solution:
    def minChanges(self, s: str) -> int:
        min_changes_required = 0

        # Check pairs of characters (i, i+1) with step size 2
        for i in range(0, len(s), 2):
            # If characters in current pair don't match,
            # we need one change to make them equal
            if s[i] != s[i + 1]:
                min_changes_required += 1
        return min_changes_required