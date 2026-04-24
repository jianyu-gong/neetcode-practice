class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c == "+":
                temp = stack.pop() + stack.pop()
                stack.append(temp)
            elif c == "-":
                temp = -stack.pop() + stack.pop()
                stack.append(temp)
            elif c == "*":
                temp = stack.pop() * stack.pop()
                stack.append(temp)
            elif c == '/':
                temp = float(1/stack.pop()) * stack.pop()
                stack.append(temp)
            else:
                stack.append(int(c))

        return int(stack[0])

        