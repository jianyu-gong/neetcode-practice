class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        global_max = global_min = nums[0]
        current_sum_max = current_sum_min = 0

        total = 0

        for n in nums:
            
            current_sum_max = max(n, current_sum_max + n)

            global_max = max(current_sum_max, global_max)

            current_sum_min = min(n, current_sum_min + n)
            
            global_min = min(global_min, current_sum_min)

            total += n
            

        if global_max < 0:
            return global_max

        else:
            return max(global_max, total - global_min)