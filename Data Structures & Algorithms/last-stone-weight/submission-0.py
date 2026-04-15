class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # print(f'before, {stones=}')
        heapq.heapify_max(stones)

        # print(f'after, {stones=}, {len(stones)}')

        while len(stones) > 1:
            x = heapq.heappop_max(stones)
            y = heapq.heappop_max(stones)

            if x != y:
                heapq.heappush_max(stones, abs(x-y))


        return stones[0] if len(stones) == 1 else 0