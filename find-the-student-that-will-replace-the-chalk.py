"""
find-the-student-that-will-replace-the-chalk.py
"""
from typing import List

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        sm_chalk = sum(chalk)
        k %= sm_chalk

        for i in range(len(chalk)):
            if k < chalk[i]:
                return i
            k -= chalk[i]

        # sm_chalk = sum(chalk)
        # j = 1
        # while True:
        #     if j * sm_chalk < k:
        #         k -= (sm_chalk * j)
        #         j+=1
        #     else:
        #         for i in range(len(chalk)):
        #             if k < chalk[i]:
        #                 return i
        #             k -= chalk[i]
