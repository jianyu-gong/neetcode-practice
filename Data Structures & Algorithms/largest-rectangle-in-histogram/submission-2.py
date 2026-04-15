class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        num_of_bar = len(heights)
        res = 0

        stack = []

        for i, h in enumerate(heights):
            start = i
            while len(stack) > 0 and stack[-1][-1] > heights[i]:
                index, height = stack.pop()

                res = max(res, height * (i - index))
            
                start = index
            
            stack.append((start, h))
            # print(f'{stack=}')

        for i, h in stack:
            # print(f'{i=}, {(num_of_bar-i)*h}')
            res = max(res, h * (num_of_bar-i))
            

        return res



