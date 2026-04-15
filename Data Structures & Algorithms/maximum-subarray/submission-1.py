class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        current_max_sum = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            
            if current_max_sum < 0:
                current_max_sum = 0

            current_max_sum = current_max_sum + nums[i]
            res = max(res, current_max_sum)
        return res