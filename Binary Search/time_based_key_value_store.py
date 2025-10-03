from collections import defaultdict

class TimeMap:
    def __init__(self):
        self.hashmap = defaultdict(lambda: ([], {}))
    def set(self, key: str, value: str, timestamp: int) -> None:
        stamps, values = self.hashmap[key]
        stamps.append(timestamp)
        values[timestamp] = value
    def get(self, key: str, timestamp: int) -> str:
        stamps, values = self.hashmap[key]
        if not stamps:
            return ""

        l, r = 0, len(stamps) - 1
        ans = ""
        while l <= r:
            m = (l + r) // 2
            if stamps[m] == timestamp:
                return values[stamps[m]]
            elif stamps[m] < timestamp:
                ans = values[stamps[m]]
                l = m + 1
            else:
                r = m - 1

        return ans
