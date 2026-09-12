"""
insert-greatest-common-divisors-in-linked-list.py
2807. Insert Greatest Common Divisors in Linked List
Solved
Medium
Topics
Companies
Given the head of a linked list head, in which each node contains an integer value.

Between every pair of adjacent nodes, insert a new node with a value equal to the greatest common divisor of them.

Return the linked list after insertion.

The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.
"""
# Definition for singly-linked list.
from typing import List, Optional
from math import gcd
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current.next:
            gcd_val = gcd(current.next.val, current.val)
            inBetwNode = ListNode(val=gcd_val, next=current.next)
            current.next = inBetwNode
            current = current.next.next
        return head