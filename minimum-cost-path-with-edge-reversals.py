"""
Docstring for 2026.day 2.minimum-cost-path-with-edge-reversals
3650. Minimum Cost Path with Edge Reversals
Solved
Medium
Topics
premium lock icon
Companies
Hint
You are given a directed, weighted graph with n nodes labeled from 0 to n - 1, and an array edges where edges[i] = [ui, vi, wi] represents a directed edge from node ui to node vi with cost wi.

Each node ui has a switch that can be used at most once: when you arrive at ui and have not yet used its switch, you may activate it on one of its incoming edges vi → ui reverse that edge to ui → vi and immediately traverse it.

The reversal is only valid for that single move, and using a reversed edge costs 2 * wi.

Return the minimum total cost to travel from node 0 to node n - 1. If it is not possible, return -1.

"""



import List, heapq,inf

class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for x, y, w in edges:
            g[x].append((y, w))
            g[y].append((x, 2 * w))

        dist = [inf] * n
        visited = [False] * n
        dist[0] = 0
        heap = [(0, 0)]  # (Distance, Node)

        while heap:
            cur_dist, x = heapq.heappop(heap)

            if x == n - 1:
                return cur_dist

            # already processed
            if visited[x]:
                continue
            visited[x] = True

            # relaxing neighbors
            for y, w in g[x]:
                new_dist = cur_dist + w
                if new_dist < dist[y]:
                    dist[y] = new_dist
                    heapq.heappush(heap, (new_dist, y))

        return -1