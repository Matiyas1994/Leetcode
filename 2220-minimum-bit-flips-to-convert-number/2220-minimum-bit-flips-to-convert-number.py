class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        n = start ^ goal
        count = 0
        while (n):
            n = n & (n-1)
            count +=1
            
        return count
        
        