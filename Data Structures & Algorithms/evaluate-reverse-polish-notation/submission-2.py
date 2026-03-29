class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c not in "+-*/":
                stack.append(int(c))
            elif c == '+':
                r = stack.pop()
                l = stack.pop()
                stack.append(l + r)
            elif c == '-':
                r = stack.pop()
                l = stack.pop()
                stack.append(l - r)
            elif c == '*':
                r = stack.pop()
                l = stack.pop()
                stack.append(l * r)
            elif c == '/':
                r = stack.pop()
                l = stack.pop()
                stack.append(int(l / r))

        return int(stack[0])