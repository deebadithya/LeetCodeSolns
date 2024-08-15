"""
lemonade-change.py
860. Lemonade Change
Solved
Easy
Topics
Companies
At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. You must provide the correct change to each customer so that the net transaction is that the customer pays $5.

Note that you do not have any change in hand at first.

Given an integer array bills where bills[i] is the bill the ith customer pays, return true if you can provide every customer with the correct change, or false otherwise.
"""
from typing import List
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cnt5, cnt10=0, 0
        for b in bills:
            if b==5: cnt5+=1
            elif b==10:
                if cnt5>0:
                    cnt5-=1
                    cnt10+=1
                else:
                    return False
            else:
                if cnt10>0 and cnt5>0:
                    cnt10-=1
                    cnt5-=1
                elif cnt5>2: cnt5-=3
                else: return False
        return True