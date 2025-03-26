"""
minimum-operations-to-make-a-uni-value-grid.py
2033. Minimum Operations to Make a Uni-Value Grid
Solved
Medium
Topics
Companies
Hint
You are given a 2D integer grid of size m x n and an integer x. In one operation, you can add x to or subtract x from any element in the grid.

A uni-value grid is a grid where all the elements of it are equal.

Return the minimum number of operations to make the grid uni-value. If it is not possible, return -1.
"""
from typing import List
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        grid = sorted([val for row in grid for val in row])
        mid = len(grid) // 2
        stepCount = 0
        for i in range(len(grid)):
            if grid[i] % x == grid[mid] % x :  
                stepCount += abs( ( grid[mid] - grid[i] ) ) // x 
            else:
                return -1
        return stepCount