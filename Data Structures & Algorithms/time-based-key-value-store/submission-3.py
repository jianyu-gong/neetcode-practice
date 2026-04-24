class TimeMap:

    def __init__(self):
        self.mood = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mood:
            self.mood[key] = [(timestamp, value)]

        else:
            self.mood[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.mood:
            return ''

        mood_list = self.mood[key]
        
        left = 0
        right = len(mood_list) - 1
        res = mood_list[left][1]

        while left <= right:
            
            mid = (left + right) // 2

            if mood_list[mid][0] <= timestamp:
                res = mood_list[left][1]
                left = mid + 1
            else:
                right = mid - 1
            print(f'after: {left=}, {right=}')

        return res
