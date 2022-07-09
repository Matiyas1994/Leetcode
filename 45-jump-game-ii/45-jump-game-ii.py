class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp=[float("inf") for _ in range(n)]
        dp[0]=0
        canreach = defaultdict(list)
        
        for k in range(1,nums[0]+1):
                canreach[k].append(0)
        
        for i in range(1,n):
            for j in canreach[i]:
                dp[i] = min(dp[i], dp[j]+1)
            for k in range(1,nums[i]+1):
                canreach[i+k].append(i)
            
        return dp[-1]
                
        
        
        
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
        
        