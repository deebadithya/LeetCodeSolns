"""
spiral-matrix-iv.py
2326. Spiral Matrix IV
Solved
Medium
Topics
Companies
Hint
You are given two integers m and n, which represent the dimensions of a matrix.

You are also given the head of a linked list of integers.

Generate an m x n matrix that contains the integers in the linked list presented in spiral order (clockwise), starting from the top-left of the matrix. If there are remaining empty spaces, fill them with -1.

Return the generated matrix.
"""
 # Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import List, Optional
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        result = [[-1]*n for i in range(m)]
        st, end = [0,0], [m-1, n-1]


        while head:
            for col in range(st[1], end[1]+1):
                if not head:
                    break
                result[st[0]][col] = head.val
                head = head.next
            st[0] += 1

            for row in range(st[0], end[0]+1):
                if not head:
                    break
                result[row][end[1]] = head.val
                head = head.next

            end[1] -= 1

            for col in range(end[1], st[1]-1, -1):
                if not head:
                    break
                result[end[0]][col] = head.val
                head = head.next
            end[0] -= 1

            for row in range(end[0], st[0]-1, -1):
                if not head:
                    break
                result[row][st[1]] = head.val
                head = head.next
            st[1] += 1

        return result

                


