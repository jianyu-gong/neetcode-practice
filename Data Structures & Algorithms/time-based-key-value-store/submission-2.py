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

        # print(left, right)
        while left < right - 1:
            
            print(left, right, timestamp)

            mid = (left + right) // 2

            if timestamp > mood_list[mid][0]:
                right = mid
            elif timestamp < mood_list[mid][0]:
                left = mid + 1

            else:
                return mood_list[mid][-1]

        
        if timestamp < mood_list[left][0]:
            return ''
        elif timestamp >= mood_list[right][0]:
            return mood_list[right][1]
        else:
            return mood_list[left][1]
        # return mood_list[0][1]
