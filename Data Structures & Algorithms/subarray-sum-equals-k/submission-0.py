class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_map = {0:1}
        prefix_sum = 0
        res = 0

        for n in nums:
            prefix_sum += n
            res += prefix_map.get(prefix_sum - k, 0)
            prefix_map[prefix_sum] = 1 +  prefix_map.get(prefix_sum, 0)

        return res

        