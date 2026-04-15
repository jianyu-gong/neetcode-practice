class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            if len(stack) == 0:
                stack.append((i, temperatures[i]))
            elif temperatures[i] <= stack[-1][-1]:
                stack.append((i, temperatures[i]))
            else:
                while len(stack) > 0 and temperatures[i] > stack[-1][-1]:
                    temp = stack.pop()
                    res[temp[0]] = i - temp[0]
                stack.append((i, temperatures[i]))

            # print(stack)

        return res
        