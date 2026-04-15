class Solution:
    def trap(self, height: List[int]) -> int:

        l = 0
        r = len(height) - 1
        maxL = height[0]
        maxR = height[-1]
        area_sum = 0

        while l < r:
            if maxL <= maxR:
                area_sum += max(0, min(maxL, maxR) - height[l])
                l += 1
                maxL = max(maxL, height[l])

            else:
                area_sum += max(0, min(maxL, maxR) - height[r])
                r -= 1
                maxR = max(maxR, height[r])
            
        return area_sum
        