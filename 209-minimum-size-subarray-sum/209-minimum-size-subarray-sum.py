class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # [2, 3, 1, 2, 4, 3]
        #           p1  
        #                 p2 
        # _sum = 6
        # ans = 3
        p1, p2 = 0, 0
        n = len(nums)
        ans = float(inf)
        _sum = 0
        while p2 < n:
            while p2 < n and _sum < target:
                _sum += nums[p2] 
                p2 +=1
            while _sum >= target:
                ans= min(ans, p2-p1)
                _sum -= nums[p1]
                p1 +=1
                
            
        
        return 0 if ans == float(inf) else ans
        
        