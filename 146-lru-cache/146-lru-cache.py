class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.Odic = OrderedDict()
    
    def get(self, key: int) -> int:
        if key in self.Odic: self.Odic[key] = self.Odic.pop(key)
        return self.Odic[key] if key in self.Odic else -1    

    def put(self, key: int, value: int) -> None:
        if key in self.Odic:
            self.Odic.pop(key)
            self.Odic[key] = value
        else:
            if len(self.Odic) >= self.capacity:
                self.Odic.popitem(last=False)
            self.Odic[key] = value
          
                
                
            
            
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)