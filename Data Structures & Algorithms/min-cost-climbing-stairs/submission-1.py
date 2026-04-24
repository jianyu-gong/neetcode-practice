class Solution:
    # def __init__(self):
    #     self.cache = {}

    def minCostClimbingStairs(self, cost: List[int]) -> int:
          
        length = len(cost)
        # cache = {}

        # if length <= 2:
        #     return min(cost)

        # cache[length - 1] = cost[-1]
        # cache[length - 2] = cost[-2]


        # for i in range(length-3, -1, -1):
            
        #     cache[i] = cost[i] + min(cache[i+1], cache[i+2])

        cost.append(0)

        for i in range(length-3, -1, -1):
            cost[i] += min(cost[i+1], cost[i+2])



        # return min(cache[0], cache[1])
        return min(cost[0], cost[1])
