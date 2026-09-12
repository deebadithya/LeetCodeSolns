"""
find-the-length-of-the-longest-common-prefix.py
"""
from bisect import bisect_left
from typing import List
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        def comman_prefix(str1, str2):
            length = min(len(str1), len(str2))
            
            for i in range(length):
                if str1[i] != str2[i]:
                    return i
            return length
        
        arr1 = [str(x) for x in arr1]
        arr2 = [str(x) for x in arr2]

        arr1.sort()
        arr2.sort()

        maximum_longest = 0
        for str_1 in arr1:
            idx = bisect_left(arr2, str_1)

            if idx < len(arr2):
                maximum_longest = max(maximum_longest, comman_prefix(str_1, arr2[idx]))
            if idx > 0 :
                maximum_longest = max(maximum_longest, comman_prefix(str_1, arr2[idx-1]))
        return maximum_longest


#         longest = 0
#         arr1, arr2 = [str(ele) for ele in set(arr1)], [str(ele) for ele in set(arr2)]
#         for str_1 in arr1:
#             for str_2 in arr2:
#                 while str_1[longest:] and str_2[longest:] and str_1[:longest+1] == str_2[:longest+1]:
#                     longest += 1
#         return longest
soln = Solution()
#current = from_list([5,4,8,11,None,13,4,7,2,None,None,None,1])
result = soln.longestCommonPrefix([13,27,45], [21,27,48])
print(result)
