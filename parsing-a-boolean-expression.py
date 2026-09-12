"""
parsing-a-boolean-expression.py
1106. Parsing A Boolean Expression
Solved
Hard
Topics
Companies
Hint
A boolean expression is an expression that evaluates to either true or false. It can be in one of the following shapes:

't' that evaluates to true.
'f' that evaluates to false.
'!(subExpr)' that evaluates to the logical NOT of the inner expression subExpr.
'&(subExpr1, subExpr2, ..., subExprn)' that evaluates to the logical AND of the inner expressions subExpr1, subExpr2, ..., subExprn where n >= 1.
'|(subExpr1, subExpr2, ..., subExprn)' that evaluates to the logical OR of the inner expressions subExpr1, subExpr2, ..., subExprn where n >= 1.
Given a string expression that represents a boolean expression, return the evaluation of that expression.
It is guaranteed that the given expression is valid and follows the given rules.
"""
from collections import deque
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        st = deque()
        for c in expression:
            if c == '(' or c == ',':
                continue
            elif c in ['&', '!', '|', 't', 'f']:
                st.append(c)
            elif c == ')':
                has_true = False
                has_false = False
                while c not in ['&', '|', '!']:
                    top_val = st.pop()
                    if top_val == 't':
                        has_true = True
                    elif top_val == 'f':
                        has_false = True
                exp = st.pop()
                if exp == '&':
                    st.append('f' if has_false else 't')
                elif exp == '|':
                    st.append('t' if has_true else 'f')
                else:
                    st.append('t' if not has_true else 'f')
        return st[-1] == 't'