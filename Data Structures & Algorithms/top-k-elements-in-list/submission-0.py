class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = {}

        for n in nums:
            if n in count_map:
                count_map[n] += 1
            else:
                count_map[n] = 1

        sorted_count_map_desc = sorted(count_map.items(), key=lambda item: item[1], reverse=True)

        key_list = [k[0] for k in sorted_count_map_desc]

        return key_list[:k]

