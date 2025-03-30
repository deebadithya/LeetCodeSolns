"""
partition-labels.py
"""

from typing import List
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}

        for i, e in enumerate(s):
            lastIndex[e] = i

        size, end = 0, 0
        res = []

        for i, c in enumerate(s):
            size += 1

            end = max(lastIndex[c], end)

            if i == end:
                res.append(size)
                size = 0

        return res

soln = Solution()
result = soln.partitionLabels("ababcbacadefegdehijhklij")
print(result)