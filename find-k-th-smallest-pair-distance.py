"""
find-k-th-smallest-pair-distance.py
"""
from typing import List
import heapq
def smallestDistancePair(nums: List[int], k: int) -> int:
    ls = []
    # heapq.heapify(ls)
    l_nums = len(nums)
    for st in range(l_nums - 1):
        for ele in range(st+1, l_nums):
            # heapq.heappush(ls, abs( nums[st] - nums[ele]  ))       
            ls.append(abs( nums[st] - nums[ele]  ))
        # if len(ls) >= k:
        #     return ls[k-1]
    return sorted(ls)[k-1]
    # print(len(ls))
    # while len(ls) > 0:
    #     print(heapq.heappop(ls), end=" ")

print(smallestDistancePair([9,10,7,10,6,1,5,4,9,8], 18))