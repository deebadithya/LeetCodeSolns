"""
5. Longest Palindromic Substring
Solved
Medium
Topics
Companies
Hint
Given a string s, return the longest 
palindromic
 
substring
 in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        prev = None
        current = s[0]
        paline = current

        def is_paline(i, j=0, init=1):
            while(i-init-j>=0 and i+init < len(s)):
                
                if (s[i-init-j] != s[i+init]):
                    break
                paline = s[i - init -j : i + init + 1]
                init +=1
            return paline

        for i in range(1,len(s)):
            nextl = s[i]
        
            if current == nextl:
                result = is_paline(i, j=1, init=0)
                if len(result) > len(paline):
                    paline = result
                
            if prev == nextl:
                result = is_paline(i-1)
                if len(result) > len(paline):
                    paline = result
            prev = current
            current = nextl
        return paline
            
                
                
                
                    
                

                





            


        