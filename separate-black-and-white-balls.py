"""
separate-black-and-white-balls.py
"""
class Solution:
    def minimumSteps(self, s: str) -> int:
        black, swap = 0, 0
        for c in s:
            if c == '0':
                swap += black
            else:
                black +=1
        return swap