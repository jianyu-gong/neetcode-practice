class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check_list = []

        for n in nums:
            if n in check_list:
                return True
            else:
                check_list.append(n)

        return False