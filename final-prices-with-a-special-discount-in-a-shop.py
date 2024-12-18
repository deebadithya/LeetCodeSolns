"""
final-prices-with-a-special-discount-in-a-shop
1475. Final Prices With a Special Discount in a Shop
Solved
Easy
Topics
Companies
Hint
You are given an integer array prices where prices[i] is the price of the ith item in a shop.

There is a special discount for items in the shop. If you buy the ith item, then you will receive a discount equivalent to prices[j] where j is the minimum index such that j > i and prices[j] <= prices[i]. Otherwise, you will not receive any discount at all.

Return an integer array answer where answer[i] is the final price you will pay for the ith item of the shop, considering the special discount.

 
"""
from typing import List
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        result = prices
        for i in range(len(prices)-1):
            for j in range(i+1, len(prices)):
                if prices[i] >= prices[j]:
                    result[i] -= prices[j]
                    break
        return result