"""
lexicographical-numbers.py
386. Lexicographical Numbers
Solved
Medium
Topics
Companies
Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.
You must write an algorithm that runs in O(n) time and uses O(1) extra space.
"""
from typing import List
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        # ls = [[], [], [], [], [], [], [], [], [], []]
        # for i in range(1,n+1):
        #     ls[int(str(i)[0])].append(i)
        
        # return ls[0] + ls[1] + ls[2] + ls[3] + ls[4] + ls[5] + ls[6] + ls[7] + ls[8] + ls[9]
    
        return list(map(int, sorted(list(map(str, list(range(1, n+1)))))))
        



        