class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp=[float("inf") for _ in range(n)]
        dp[-1]=0
        
        for i in range(n-2,-1,-1):
            for j in range(1,nums[i]+1):
                if j+i <= n-1:
                    dp[i] = min(dp[i], dp[i+j]+1)
            
        return dp[0]
                
        
        
        
#         memo = {}
#         def minijump(idx = 0):
#             if idx >= len(nums)-1:
#                 return 0
#             if idx in memo:
#                 return memo[idx]
#             res = float(inf)
#             for i in range(1,nums[idx]+1):
#                 res = min(minijump(idx + i),res)
#             memo[idx] =  res + 1
#             return memo[idx]
        
#         return minijump()
        
        