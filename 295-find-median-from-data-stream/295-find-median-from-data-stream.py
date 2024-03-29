class MedianFinder:

    def __init__(self):
        self.left =[]
        self.right = []

    def addNum(self, num: int) -> None:
        if self.left and num <= -self.left[0]:
            heapq.heappush(self.left, -num)
        else:
            heapq.heappush(self.right, num)
        
        while len(self.left) > len(self.right)+1:
            t = heapq.heappop(self.left)
            heapq.heappush(self.right, -t)
            
        while len(self.right) > len(self.left)+1:
            t = heapq.heappop(self.right)
            heapq.heappush(self.left, -t)

    def findMedian(self) -> float:
        if len(self.left)==len(self.right):
            return (-self.left[0] + self.right[0])/2
        elif len(self.left) > len(self.right):
            return -self.left[0]
        return self.right[0]
            

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()