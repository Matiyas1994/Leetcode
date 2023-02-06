class DetectSquares:

    def __init__(self):
        self.points = defaultdict(lambda: defaultdict(int))

    def add(self, point: List[int]) -> None:
        self.points[point[0]][point[1]] +=1
        

    def count(self, point: List[int]) -> int:
        ans = 0
        for sameRow, k in self.points[point[0]].items():
            if sameRow == point[1]: continue
            dif = abs(point[1]-sameRow)
            toright = self.points[point[0]+dif][point[1]]
            toleft = self.points[point[0]-dif][point[1]]
            downleft = self.points[point[0]-dif][sameRow]
            downright = self.points[point[0]+dif][sameRow]
            
            ans += toright*downright * k + toleft*downleft * k
        
        return ans
            


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)