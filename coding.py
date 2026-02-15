"""
Problem: Valid Parentheses

Given a string containing just the characters:
'(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

A string is valid if:
1. Open brackets are closed by the same type.
2. Open brackets are closed in the correct order.

Approach:
- Use a stack to track opening brackets.
- When encountering a closing bracket:
  - Check if stack is empty or mismatch → invalid.
- At the end, stack should be empty.

Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in mapping:
                if not stack or stack.pop() != mapping[char]:
                    return False
            else:
                stack.append(char)
        return not stack
