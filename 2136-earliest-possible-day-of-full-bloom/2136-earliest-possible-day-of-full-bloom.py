class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        zipped =list(zip(plantTime, growTime))
        zipped.sort(key = lambda x: x[1], reverse = True)
        maxDay = 0
        prev = 0
        for i in range(len(zipped)):
            prev += zipped[i][0]
            maxDay = max(maxDay, prev+zipped[i][1])
        return maxDay
        
        
        
        