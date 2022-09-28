class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        maxOnes, lastZero, j = 0, [], 0
        for i in range(len(nums)):
            if nums[i]==0:
                heapq.heappush(lastZero,i)
                k -=1
            if k < 0:
                if lastZero: 
                    t = heapq.heappop(lastZero)
                k +=1
                j  = t+1
            
            maxOnes= max(maxOnes, i-j+1)
        
        return maxOnes
            