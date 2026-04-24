class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort()

        # print(pair)
        last_car = pair.pop()
        time_spend = (target - last_car[0]) // last_car[-1]
        res = 1
        print(pair)
        while len(pair) > 0:
            last_car = pair.pop()
            last_position = last_car[0]
            last_speed = last_car[-1]

            if (target - last_position) // last_speed > time_spend:
                res += 1
                time_spend = (target - last_position) // last_speed

        return res
        