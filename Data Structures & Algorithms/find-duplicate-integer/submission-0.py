class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        num_set = set()

        for n in nums:
            if n in num_set:
                return n
            num_set.add(n)

        