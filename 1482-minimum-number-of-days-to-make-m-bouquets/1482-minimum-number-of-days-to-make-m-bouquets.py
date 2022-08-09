class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def helper(gussedDate, numOfBuqetThatShouldBeMade, k):
            bucket = 0
            t = 0
            for i in range(len(bloomDay)):
                if bloomDay[i] <= gussedDate:
                    t +=1
                    if t == k:
                        t = 0
                        bucket +=1
                else:
                    t = 0
                   
            return bucket >= numOfBuqetThatShouldBeMade
        
        
        low, high = min(bloomDay), max(bloomDay)
        ans = -1
        while low<=high:
            mid = low + (high-low)//2
            
            if helper(mid, m, k ):
                ans = mid
                high = mid-1
            else: 
                low = mid+1
        
        return ans
    
        