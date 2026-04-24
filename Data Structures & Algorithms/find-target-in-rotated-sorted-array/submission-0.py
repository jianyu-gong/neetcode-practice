class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left < right - 1:

            mid = (left + right) // 2
            
            if nums[mid] > nums[right]:
                left = mid

            else:
                right = mid

        
        if nums[left] > nums[right]:
            minimum_index = right

        else:
            minimum_index = left

        if target == nums[minimum_index]:
            return minimum_index

        if nums[minimum_index] < target < nums[-1]:
            start = minimum_index
            end = len(nums)

        else:
            start = 0
            end = minimum_index

        for i in range(start, end):
            if nums[i] == target:

                return i

        return -1    

        return 1

        