"""
find-champion-ii.py
"""
from typing import List

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        status = [0] * n
        for st,ed in edges:
            status[ed] = 1
        if status.count(0) == 1:
            return status.index(0)
        return -1
            
