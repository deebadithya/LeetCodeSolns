"""
xor-queries-of-a-subarray.py
1310. XOR Queries of a Subarray
Solved
Medium
Topics
Companies
Hint
You are given an array arr of positive integers. You are also given the array queries where queries[i] = [lefti, righti].

For each query i compute the XOR of elements from lefti to righti (that is, arr[lefti] XOR arr[lefti + 1] XOR ... XOR arr[righti] ).

Return an array answer where answer[i] is the answer to the ith query.
"""
from typing import List
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        pre = [0] * n
        pre[0] = arr[0]
        
        # Compute prefix XOR array
        for i in range(1, n):
            pre[i] = pre[i - 1] ^ arr[i]
        
        res = []
        
        # Answer each query
        for left, right in queries:
            if left == 0:
                res.append(pre[right])
            else:
                res.append(pre[right] ^ pre[left - 1])
        
        return res
        