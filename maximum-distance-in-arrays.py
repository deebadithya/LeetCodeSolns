"""
maximum-distance-in-arrays.py
624. Maximum Distance in Arrays
Solved
Medium
Topics
Companies
You are given m arrays, where each array is sorted in ascending order.

You can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define the distance between two integers a and b to be their absolute difference |a - b|.

Return the maximum distance.
"""
from typing import List
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        smallest = arrays[0][0]
        largest = arrays[0][-1]
        max_dist = 0
        for i in range(1, len(arrays)):
            arr = arrays[i]
            max_dist = max(max_dist, abs(arr[-1] - smallest), abs( largest - arr[0]))
            smallest = min(smallest, arr[0])
            largest = max(largest, arr[-1])
        return max_dist