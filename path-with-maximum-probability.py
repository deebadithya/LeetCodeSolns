"""
path-with-maximum-probability.py
"""
from typing import List
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        dist = [0] * n
        dist[start] = 1
        
        for _ in range(n - 1):
            updated = False
            for i, (u, v) in enumerate(edges):
                if dist[u] * succProb[i] > dist[v]:
                    dist[v] = dist[u] * succProb[i]
                    updated = True
                if dist[v] * succProb[i] > dist[u]:
                    dist[u] = dist[v] * succProb[i]
                    updated = True
            if not updated:
                break
        
        return dist[end]

# class Solution:
#     def maxProbability(self, n, edges, succProb, start, end):
#         dist = [0] * n
#         dist[start] = 1
#         unfinished = []
#         ready = [dist[start],]
#         for i,(u,v) in enumerate(edges):
#             res1 = dist[u] * succProb[i]
#             res2 = dist[v] * succProb[i]
#             if res1 > res2:
#                 dist[v] = res1
#             else:
#                 dist[u] = res2
#         return dist[end]
                

# class Solution:
#     def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
#         node_struc = {}
#         for i in range(len(edges)):
#             if edges[i][0] not in node_struc:
#                 node_struc[ edges[i][0] ] =  {edges[i][1]: succProb[i]} 
#             else:
#                 temp = node_struc[ edges[i][0] ]
#                 temp[edges[i][1]] = succProb[i]
#                 node_struc[ edges[i][0] ] = temp
#         def dfs(current_node):
#             init = 0
#             if current_node == end_node:
#                 return 1
#             elif current_node not in node_struc: return 0

#             for ch in node_struc[current_node]:
#                 result = node_struc[current_node][ch] * dfs(ch)
#                 if result > init:
#                     init = result
#             return init
#         return dfs(start_node)
soln  = Solution()
result = soln.maxProbability(3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.2], 0, 2)
# result = soln.maxProbability(3, [[0,1]], [0.5], 0, 2)
print(result)

