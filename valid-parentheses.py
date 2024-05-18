"""
valid-parentheses


Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""
class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for i in s:
            if i == '[' or i == '{' or i == '(':
                st.append(i)
            elif st:
                if i=="}":
                    if st[-1] != '{':
                        return False
                    st.pop()         
                elif i=="]":
                    if st[-1] != '[':
                        return False
                    st.pop()
                elif i==')':
                    if st[-1] != '(':
                        return False
                    st.pop()
            else:
                return False
        if st:
            return False
        else:
            return True