"""
sum-of-digits-of-string-after-convert.py
1945. Sum of Digits of String After Convert
Solved
Easy
Topics
Companies
Hint
You are given a string s consisting of lowercase English letters, and an integer k.

First, convert s into an integer by replacing each letter with its position in the alphabet (i.e., replace 'a' with 1, 'b' with 2, ..., 'z' with 26). Then, transform the integer by replacing it with the sum of its digits. Repeat the transform operation k times in total.

For example, if s = "zbax" and k = 2, then the resulting integer would be 8 by the following operations:

Convert: "zbax" ➝ "(26)(2)(1)(24)" ➝ "262124" ➝ 262124
Transform #1: 262124 ➝ 2 + 6 + 2 + 1 + 2 + 4 ➝ 17
Transform #2: 17 ➝ 1 + 7 ➝ 8
Return the resulting integer after performing the operations described above.
"""
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        s_num = ""
        for ch in s:
            s_num += str(ord(ch) - 96) 
        result = s_num
        for nth in range(k):
            result = 0
            for ch in s_num:
                result += int(ch) 
            s_num = str(result)
        return result
    
# Solution Link
# https://leetcode.com/problems/sum-of-digits-of-string-after-convert/solutions/5731382/simple-and-efficient-solution-beats-100-users-python