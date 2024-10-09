"""
minimum-add-to-make-parentheses-valid.py
"""
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        extras = 0
        result = 0
        for ch in s:
            if ch == '(':
                result += 1
            elif result > 0:
                result -= 1
            else:
                extras += 1
                
            
        return result + extras
        