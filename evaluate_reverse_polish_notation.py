class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        if len(tokens) > 1:
            for ch in tokens:
                if ch  not in "+-*/":
                    stack.append(ch)
                else:
                    x = int(stack.pop())
                    y = int(stack.pop())
                    if ch == "+":
                        stack.append(x+y)
                    elif ch == "-":
                        stack.append(y-x)
                    elif ch == "*":
                        stack.append(x*y)
                    elif ch == "/":
                        stack.append(y/x)
            return int(stack[-1])
        return int(tokens[0])