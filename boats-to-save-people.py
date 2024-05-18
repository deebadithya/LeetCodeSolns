"""
boats-to-save-people

881. Boats to Save People
Solved
Medium
Topics
Companies
You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.

 

Example 1:

Input: people = [1,2], limit = 3
Output: 1
Explanation: 1 boat (1, 2)
Example 2:

Input: people = [3,2,2,1], limit = 3
Output: 3
Explanation: 3 boats (1, 2), (2) and (3)
Example 3:

Input: people = [3,5,3,4], limit = 5
Output: 4
Explanation: 4 boats (3), (3), (4), (5)
 

Constraints:

1 <= people.length <= 5 * 104
1 <= people[i] <= limit <= 3 * 104
"""
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        # Initialize two pointers, one at the beginning and one at the end of the array
        left = 0  # Pointer for the lightest person
        right = len(people) - 1  # Pointer for the heaviest person
        boats_count = 0  
        
        # Iterate until both pointers meet or cross each other
        while left <= right:
            if people[left] + people[right] <= limit:
                boats_count += 1  
                left += 1  
                right -= 1  
            elif people[right] <= limit:
                boats_count += 1  
                right -= 1  

        return boats_count  
        


                
        
       
        


            
