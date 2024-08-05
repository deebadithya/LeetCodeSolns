"""
kth-distinct-string-in-an-array.py
2053. Kth Distinct String in an Array
Solved
Easy
Topics
Companies
Hint
A distinct string is a string that is present only once in an array.

Given an array of strings arr, and an integer k, return the kth distinct string present in arr. If there are fewer than k distinct strings, return an empty string "".

Note that the strings are considered in the order in which they appear in the array.
"""
from typing import List
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        uni_eles = []
        dups = []
        for ele in arr:
            if ele in uni_eles:
                uni_eles.remove(ele)
                dups.append(ele)
            else:
                if ele not in dups:
                    uni_eles.append(ele)
        if len(uni_eles) >= k:
            return uni_eles[k-1]
        return ""