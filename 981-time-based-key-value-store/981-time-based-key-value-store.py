class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)
        
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        heapq.heappush(self.timeMap[key], (-1*timestamp, value))
        
        
    def get(self, key: str, timestamp: int) -> str:
        ans = ""
        if key not in self.timeMap:
            return ""
        t = []
        
        while self.timeMap[key] and -1*self.timeMap[key][0][0] > timestamp:
            t.append(heapq.heappop(self.timeMap[key]))
        if not self.timeMap[key]:
            ans = ""
        else:
            ans =  self.timeMap[key][0][1]
        while t :
             heapq.heappush(self.timeMap[key],t.pop())
        
        return ans
            


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)