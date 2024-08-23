"""
fraction-addition-and-subtraction.py

Code
Testcase
Test Result
Test Result
592. Fraction Addition and Subtraction
Solved
Medium
Topics
Companies
Given a string expression representing an expression of fraction addition and subtraction, return the calculation result in string format.

The final result should be an irreducible fraction. If your final result is an integer, change it to the format of a fraction that has a denominator 1. So in this case, 2 should be converted to 2/1.
"""
import re
from math import gcd
class Solution:
    def fractionAddition(self, expression: str) -> str:
        nums = list(map(int, re.findall(r'[+-]?\d+', expression)))
        numerator = 0
        denominator = 1
        
        for i in range(0, len(nums), 2):
            num, den = nums[i], nums[i + 1]
            numerator = numerator * den + num * denominator
            denominator *= den
        
        common_divisor = gcd(numerator, denominator)
        return f"{numerator // common_divisor}/{denominator // common_divisor}" 