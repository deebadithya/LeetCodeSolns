"""
divide-players-into-teams-of-equal-skill.py
2491. Divide Players Into Teams of Equal Skill
Solved
Medium
Topics
Companies
Hint
You are given a positive integer array skill of even length n where skill[i] denotes the skill of the ith player. Divide the players into n / 2 teams of size 2 such that the total skill of each team is equal.
The chemistry of a team is equal to the product of the skills of the players on that team.
Return the sum of the chemistry of all the teams, or return -1 if there is no way to divide the players into teams such that the total skill of each team is equal.
"""
from typing import List
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        
        total_skill = skill[0] + skill[-1] 
        chemistry_sum = 0

        for i in range(len(skill) // 2):
            if skill[i] + skill[-i - 1] != total_skill:
                return -1 
           
            chemistry_sum += skill[i] * skill[-i - 1]

        return chemistry_sum  