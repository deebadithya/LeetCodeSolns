"""
divide-intervals-into-minimum-number-of-groups.py
2406. Divide Intervals Into Minimum Number of Groups
Solved
Medium
Topics
Companies
Hint
You are given a 2D integer array intervals where intervals[i] = [lefti, righti] represents the inclusive interval [lefti, righti].

You have to divide the intervals into one or more groups such that each interval is in exactly one group, and no two intervals that are in the same group intersect each other.

Return the minimum number of groups you need to make.

Two intervals intersect if there is at least one common number between them. For example, the intervals [1, 5] and [5, 8] intersect.
"""
from typing import List
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        start, end = 0, 0
        start_arr, end_arr = [], []
        for i, j in intervals:
            start_arr.append(i)
            end_arr.append(j)
        start_arr.sort()
        end_arr.sort()
        result = 0
        while start < len(intervals):
            if start_arr[start] <= end_arr[end]:  
                start += 1
            else:
                end += 1
            result = max(result, start - end)

        return result