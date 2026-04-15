class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        preSum = [0] * (len(nums) + 1) 
        postSum = [0] * (len(nums) + 1) 
        
        for i in range(len(nums)):
            preSum[i+1] = preSum[i] + nums[i]

        for i in range(len(nums)-1, -1, -1):
            postSum[i] = postSum[i+1] + nums[i]

        for i in range(len(nums)):
            if preSum[i] == postSum[i + 1]:
                return i


        return -1
