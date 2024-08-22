"""
number-complement.py

Code
Testcase
Testcase
Test Result
476. Number Compleent
Solved
Easy
Topics
Companies
The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.

For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
Given an integer num, return its complement.
"""
class Solution:
    def findComplement(self, num: int) -> int:
        bit_length = num.bit_length()
        # print(bit_length)
        mask = (1 << bit_length) - 1

        return num ^ mask

