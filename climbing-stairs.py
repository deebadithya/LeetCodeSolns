"""
climbing-stairs.py
70. Climbing Stairs
Solved
Easy
Topics
Companies
Hint
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        if n==0 or n==1:
            return 1
        a,b = 1,1
        for i in range(2, n+1):
            b,a = a+b, b
        return b
        