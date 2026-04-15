class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        l = r = 0
        current_sum = 0
        res = 0

        while r < len(arr):
            if r - l >= k:
                current_sum -= arr[l]
                l += 1

            current_sum += arr[r]
            # print(current_sum, k * threshold)
            if current_sum >= k * threshold and r - l == k - 1:
                res += 1

            r += 1

        return res
                
        