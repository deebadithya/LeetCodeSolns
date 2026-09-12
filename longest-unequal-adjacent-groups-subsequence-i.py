"""
longest-unequal-adjacent-groups-subsequence-i.py
"""
from typing import List
class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        result = []
        for i in range(len(words)):
            if i == len(words) - 1:
                result.append(words[i])
                break
            if groups[i] != groups[i+1]:
                result.append(words[i])
        return result

            