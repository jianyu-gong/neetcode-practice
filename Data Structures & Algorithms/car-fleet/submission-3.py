class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort()

        res = [pair.pop()]

        while len(pair) > 0:
            last_car = pair.pop()
            time_needed = (target - last_car[0]) / last_car[-1]

            if time_needed > (target - res[-1][0]) / res[-1][-1]:
                res.append(last_car)

        return len(res)
        