"""
put-marbles-in-bags.py
2551. Put Marbles in Bags
Solved
Hard
Topics
Companies
Hint
You have k bags. You are given a 0-indexed integer array weights where weights[i] is the weight of the ith marble. You are also given the integer k.

Divide the marbles into the k bags according to the following rules:

No bag is empty.
If the ith marble and jth marble are in a bag, then all marbles with an index between the ith and jth indices should also be in that same bag.
If a bag consists of all the marbles with an index from i to j inclusively, then the cost of the bag is weights[i] + weights[j].
The score after distributing the marbles is the sum of the costs of all the k bags.

Return the difference between the maximum and minimum scores among marble distributions.

 
"""

from typing import List
class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        
        if k == 1:
            return 0

        splits = []

        for i in range(len(weights)-1):
            splits.append(weights[i]+weights[i+1])
        splits.sort()
        i = k - 1

        min_val = sum(splits[:i])
        max_val = sum(splits[-i:])

        return max_val - min_val        