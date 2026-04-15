import math


class Solution:
    def calculate_distance(self, x, y):
        return math.sqrt(x ** 2 + y ** 2)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        res = []

        heapq.heapify_max(res)

        for point in points:
            distance = self.calculate_distance(point[0], point[1])
            heapq.heappush_max(res, (distance, point))
            
            if len(res) > k:
                heapq.heappop_max(res)

        # print(res)
        return [r[-1] for r in res]


        