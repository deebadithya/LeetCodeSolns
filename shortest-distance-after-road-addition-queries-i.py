"""
shortest-distance-after-road-addition-queries-i.py
3243. Shortest Distance After Road Addition Queries I
Solved
Medium
Topics
Companies
Hint
You are given an integer n and a 2D integer array queries.

There are n cities numbered from 0 to n - 1. Initially, there is a unidirectional road from city i to city i + 1 for all 0 <= i < n - 1.

queries[i] = [ui, vi] represents the addition of a new unidirectional road from city ui to city vi. After each query, you need to find the length of the shortest path from city 0 to city n - 1.

Return an array answer where for each i in the range [0, queries.length - 1], answer[i] is the length of the shortest path from city 0 to city n - 1 after processing the first i + 1 queries.
"""
from collections import deque

class Solution:
    def bfs(self, start, end, n, graph):
        dist = [float('inf')] * n
        dist[start] = 0
        q = deque([start])

        while q:
            curr = q.popleft()
            for u in graph[curr]:
                if dist[u] > dist[curr] + 1:
                    dist[u] = dist[curr] + 1
                    q.append(u)

        return dist[end]

    def shortestDistanceAfterQueries(self, n, queries):
        answer = []
        graph = [[] for _ in range(n)]

        for i in range(n - 1):
            graph[i].append(i + 1)

        for u, v in queries:
            graph[u].append(v)
            answer.append(self.bfs(0, n - 1, n, graph))

        return answer