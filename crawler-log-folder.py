from typing import List

"""
you can find my solution at 
https://leetcode.com/problems/crawler-log-folder/solutions/5451390/simple-n-best-python-solution-easy-to-understand/
"""

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        # initizing to track the current dir position.
        loc = 0
        for log in logs:
            # checks for moving to parent dir indication else ignore.
            if log[0] == '.':
                if log[1] == '.' and loc > 0:
                    loc -= 1
            # we are going inside a directory from current directory
            else:
                loc +=1
        return loc