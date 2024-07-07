"""
water-bottles.py
1518. Water Bottles
Solved
Easy
Topics
Companies
Hint
There are numBottles water bottles that are initially full of water. You can exchange numExchange empty water bottles from the market with one full water bottle.
The operation of drinking a full water bottle turns it into an empty bottle.
Given the two integers numBottles and numExchange, return the maximum number of water bottles you can drink.
"""
# Solution 1 with normal iteration
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        counts = numBottles
        while numBottles >= numExchange:
           temp = numBottles // numExchange
           counts += temp
           numBottles = temp + numBottles % numExchange
        return counts
# Solution 2 with O(1) time and space complexity.
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        return numBottles + (numBottles-1)//(numExchange-1)
         

        