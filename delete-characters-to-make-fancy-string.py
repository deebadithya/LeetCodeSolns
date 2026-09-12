"""
delete-characters-to-make-fancy-string.py
1957. Delete Characters to Make Fancy String
Solved
Easy
Topics
Companies
Hint
A fancy string is a string where no three consecutive characters are equal.
Given a string s, delete the minimum possible number of characters from s to make it fancy.
Return the final string after the deletion. It can be shown that the answer will always be unique.
"""
class Solution:
    def makeFancyString(self, s: str) -> str:
        result = []
        counts = 1
        prev = None
        for ch in s:
            if ch == prev:
                counts += 1
            else:
                counts = 1
            prev = ch
            if counts < 3:
                result.append(ch)
        return "".join(result)
        