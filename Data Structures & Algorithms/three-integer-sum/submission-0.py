class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets = []

        self.dfs(nums, 0, 3, 0, [], subsets)
        return subsets

    def dfs(self, nums, index, k, target, subset, subsets):
        # print(subset, list(subset))

        if k == 0 and target == 0 and list(subset) not in subsets:
            subsets.append(list(subset))
            return

        if k == 0:
            return 

        for i in range(index, len(nums)):
            subset.append(nums[i])

            self.dfs(nums, i + 1, k - 1, target - nums[i], subset, subsets)

            subset.pop()