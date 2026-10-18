class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = [(timestamp,value)]
        else:
            self.store[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store: return ""
        val = self.store[key]
        if val[0][0] > timestamp: return ""
        l = 0
        r = len(val) - 1
        while l<=r:
            m = (l+r)//2
            if val[m][0] == timestamp:
                return val[m][1]
            elif val[m][0] > timestamp: r = m -1
            else: l = m + 1
        return val[l-1][1]
