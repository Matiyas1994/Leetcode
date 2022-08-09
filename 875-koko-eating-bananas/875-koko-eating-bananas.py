class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
      
        def helperAPI(gussedSpeed,shouldBeFinished):
            hrs = 0
            for i in range(len(piles)):
                hrs += math.ceil(piles[i]/gussedSpeed)
                
                if hrs > shouldBeFinished:return False
                    
            return  hrs <=shouldBeFinished
        
        low, high = 1, h*max(piles)
        ans = high
        while low<=high:
            mid = low + (high-low)//2
            
            if helperAPI(mid, h):
                ans = mid
                high = mid-1
            else:
                low = mid+1
                
        return ans
                
            
            
        
        