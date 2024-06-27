"""
find-center-of-star-graph.py
1791. Find Center of Star Graph
Solved
Easy
Topics
Companies
Hint
There is an undirected star graph consisting of n nodes labeled from 1 to n. A star graph is a graph where there is one center node and exactly n - 1 edges that connect the center node with every other node.

You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is an edge between the nodes ui and vi. Return the center of the given star graph.

"""

class Solution:
    def findCenter(self, edges) -> int:
        return edges[0][0] if (edges[0][0]==edges[-1][0] or edges[0][0]==edges[-1][1]) else edges[0][1]
        