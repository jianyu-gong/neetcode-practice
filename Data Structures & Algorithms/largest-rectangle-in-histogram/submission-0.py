class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        num_of_bar = len(heights)
        res = 0

        stack = []

        for i in range(num_of_bar):
            if len(stack) == 0:
                stack.append((i, heights[i]))

            else:
                temp_index = i
                while len(stack) > 0 and stack[-1][-1] > heights[i]:
                    temp = stack.pop()
                    # print(temp)
                    temp_area = temp[-1]*(i-temp[0])
                    # print(temp, temp_area)
                    res = max(res, temp_area)
                    temp_index -= 1
                    

                if len(stack) == 0:
                    stack.append((0, heights[i]))
                else:
                    stack.append((temp_index, heights[i]))
            # print(f'{stack=}')

        for i, h in stack:
            # print(f'{i=}, {(num_of_bar-i)*h}')
            res = max(res, h * (num_of_bar-i))
            

        return res



