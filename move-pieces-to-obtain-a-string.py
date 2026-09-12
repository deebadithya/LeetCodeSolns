"""
move-pieces-to-obtain-a-string.py
2337. Move Pieces to Obtain a String
Solved
Medium
Topics
Companies
Hint
You are given two strings start and target, both of length n. Each string consists only of the characters 'L', 'R', and '_' where:

The characters 'L' and 'R' represent pieces, where a piece 'L' can move to the left only if there is a blank space directly to its left, and a piece 'R' can move to the right only if there is a blank space directly to its right.
The character '_' represents a blank space that can be occupied by any of the 'L' or 'R' pieces.
Return true if it is possible to obtain the string target by moving the pieces of the string start any number of times. Otherwise, return false.
"""
class Solution:
    def canChange(self, s: str, t: str) -> bool:
        n=len(s)
        s+='@'
        t+='@'
        i, j=0, 0
        while i<n or j<n:
            while i<n and s[i]=='_': i+=1
            while j<n and t[j]=='_': j+=1
            c=s[i]
            if c!=t[j]: return False
            if c=='L' and i<j: return False
            if c=='R' and i>j: return False
            i+=1
            j+=1
        return True
        
        