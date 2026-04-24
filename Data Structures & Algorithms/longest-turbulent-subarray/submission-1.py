class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l, r = 0, 1

        res = 0
        pre_sign = ''

        while r < len(arr):
            if arr[r-1] > arr[r] and pre_sign != '>':
                res = max(res, r - l + 1)
                r += 1
                pre_sign = '>'

            elif arr[r-1] < arr[r] and pre_sign != '<':
                res = max(res, r - l + 1)
                r += 1
                pre_sign = '<'

            else:
                if arr[r-1] == arr[r]:
                    r += 1
                
                l = r - 1
                pre_sign = ''

        return res