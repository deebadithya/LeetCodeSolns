"""
reverse-substrings-between-each-pair-of-parentheses.py
1190. Reverse Substrings Between Each Pair of Parentheses
Solved
Medium
Topics
Companies
Hint
You are given a string s that consists of lower case English letters and brackets.
Reverse the strings in each pair of matching parentheses, starting from the innermost one.
Your result should not contain any brackets.
"""
class Solution:
    def __init__(self):
        self.i = 0
    def reverseParentheses(self, s):
        def helper(s):
            sb = []

            while self.i < len(s):
                if s[self.i] == ')':
                    self.i += 1
                    return ''.join(sb)[::-1]
                elif s[self.i] == '(':
                    self.i += 1
                    st = helper(s)
                    sb.append(st)
                else:
                    sb.append(s[self.i])
                    self.i += 1

            return ''.join(sb)

        return helper(s)