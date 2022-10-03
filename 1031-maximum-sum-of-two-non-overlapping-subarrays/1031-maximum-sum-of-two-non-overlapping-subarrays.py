class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:   
        prefix = [0]
        n = len(nums)
        
        # building Prefix sum
        for i in range(n):
            prefix.append(prefix[-1]+nums[i])
            
        
        #[ 2 ][1] and [1][  2]
        t = firstLen + secondLen
        maxSofar2, ans2 = 0,0 
        maxSoFar, ans1 = 0, 0
        for i in range(t, len(prefix)):
            maxSoFar = max(maxSoFar, prefix[i-firstLen]-prefix[i-t])
            ans1 = max(ans1, maxSoFar + prefix[i]-prefix[i-firstLen])
            maxSofar2 = max(maxSofar2, prefix[i-secondLen]-prefix[i-t])
            ans2 = max( ans2, maxSofar2 + prefix[i] - prefix[i-secondLen])
      
    
        
        return max(ans1, ans2)
        
        
            
            
            
        
        
       
              