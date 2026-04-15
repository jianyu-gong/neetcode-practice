class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        left = [1] * len(nums)
        right = [1] * len(nums)

        for i in range(1, len(nums)):
            left[i] = left[i-1] * nums[i-1]
            right[-i-1] = right[-i] * nums[-i]

        result = []
        for j in range(len(nums)):
            result.append(left[j]*right[j])

        return result