"""
adding-spaces-to-a-string.py
2109. Adding Spaces to a String
Solved
Medium
Topics
Companies
Hint
You are given a 0-indexed string s and a 0-indexed integer array spaces that describes the indices in the original string where spaces will be added. Each space should be inserted before the character at the given index.

For example, given s = "EnjoyYourCoffee" and spaces = [5, 9], we place spaces before 'Y' and 'C', which are at indices 5 and 9 respectively. Thus, we obtain "Enjoy Your Coffee".
Return the modified string after the spaces have been added.
"""
from typing import List
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = ""
        ls = 0
        for sp in spaces:
            result += s[ls:sp] + " "
            ls = sp
        return result + s[ls:]