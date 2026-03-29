class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if not stack:
                stack.append(char)
                continue

            top = stack[-1]
            if char == ')' and top == '(':
                stack.pop()
                continue
            if char == ']' and top == '[':
                stack.pop()
                continue
            if char == '}' and top == '{':
                stack.pop()
                continue
            stack.append(char)

        if len(stack) == 0:
            return True
        else:
            return False