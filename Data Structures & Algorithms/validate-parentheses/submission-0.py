class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        p_map = {
            "}": "{",
            "]": "[",
            ")": "("
        }

        for p in s:
            if p in ['{', '(', '[']:
                stack.append(p)

            else:
                if not stack or stack[-1] != p_map[p]:
                    return False

                else:
                    stack.pop()

        if len(stack) == 0:
            return True
        else:
            return False