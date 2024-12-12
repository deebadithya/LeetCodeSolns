"""
take-gifts-from-the-richest-pile.py
2558. Take Gifts From the Richest Pile
Solved
Easy
Topics
Companies
Hint
You are given an integer array gifts denoting the number of gifts in various piles. Every second, you do the following:

Choose the pile with the maximum number of gifts.
If there is more than one pile with the maximum number of gifts, choose any.
Leave behind the floor of the square root of the number of gifts in the pile. Take the rest of the gifts.
Return the number of gifts remaining after k seconds.

 
"""
from heapq import heapify, heappop, heappush
import math
from typing import List
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        nums = [-num for num in gifts]
        heapify(nums)
        while k:
            tmp = math.isqrt(-heappop(nums))
            heappush(nums,-tmp)
            k-=1
        
        return -sum(nums)