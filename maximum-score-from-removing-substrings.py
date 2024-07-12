"""
maximum-score-from-removing-substrings.py
1717. Maximum Score From Removing Substrings
Solved
Medium
Topics
Companies
Hint
You are given a string s and two integers x and y. You can perform two types of operations any number of times.

Remove substring "ab" and gain x points.
For example, when removing "ab" from "cabxbae" it becomes "cxbae".
Remove substring "ba" and gain y points.
For example, when removing "ba" from "cabxbae" it becomes "cabxe".
Return the maximum points you can gain after applying the above operations on s.
"""

class Solution:
    def cnt(self, s, target):
        res = 0
        stack = []
        for ch in s:
            if stack and ch == target[1] and stack[-1] == target[0]:
                stack.pop()
                res +=1
            else:
                stack.append(ch)
        return res, "".join(stack)
    def maximumGain(self, s: str, x: int, y: int) -> int:
        res = 0
        h_s = 'ab' if x > y else 'ba'
        l_s = 'ab' if h_s == 'ba' else 'ba'

        count_h, res_s = self.cnt(s, h_s)
        count_l, res_s = self.cnt(res_s, l_s)

        return count_h * max(x, y) + count_l * min(x, y)