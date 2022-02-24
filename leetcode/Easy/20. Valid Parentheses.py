"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
"""


class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        match_dict = {')':'(', ']':'[', '}':'{'}

        for c in s:
            if c in match_dict:
                if stack and stack[-1] == match_dict[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return len(stack)==0
        
