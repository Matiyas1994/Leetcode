class SmallestInfiniteSet:

    def __init__(self):
        self.arr = []
        self.set = set()
        for i in range(1,1001):
            self.arr.append(i)
            self.set.add(i)
        

    def popSmallest(self) -> int:
        # print(self.arr)
        smallest = heapq.heappop(self.arr)
        self.set.remove(smallest)
        return smallest
        

    def addBack(self, num: int) -> None:
        if num not in self.set:
            heapq.heappush(self.arr, num)
            self.set.add(num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)