"""
maximum-total-importance-of-roads.py
2285. Maximum Total Importance of Roads
Solved
Medium
Topics
Companies
Hint
You are given an integer n denoting the number of cities in a country. The cities are numbered from 0 to n - 1.

You are also given a 2D integer array roads where roads[i] = [ai, bi] denotes that there exists a bidirectional road connecting cities ai and bi.

You need to assign each city with an integer value from 1 to n, where each value can only be used once. The importance of a road is then defined as the sum of the values of the two cities it connects.

Return the maximum total importance of all roads possible after assigning the values optimally.

"""

# we will create an empty list <tot> has <n> 0's
# storing number of occurance of each road onto <tot> via iteration
# with the sorted list <tot> represents its priority order, returning <tot>(sorted) sum of ele * priority order( start = 1 ).



from typing import List

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        tot = [0] * n
        for a, b in roads:
            tot[a] += 1
            tot[b] += 1
        return sum( imp * val for imp, val in enumerate(sorted(tot), 1) )