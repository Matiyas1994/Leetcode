class Solution:
    def canPartition(self, nums: List[int]) -> bool:
#         memo = {}
#         def dp(target, i):
#             if target==0:
#                 return True
#             if i < 0:
#                 return False
#             if (target,i) in memo:
#                 return memo[(target,i)]
            
#             not_take = dp(target,i-1)
#             if(not_take):
#                 return True
#             take = False
#             if target-nums[i] >=0:
#                 take = dp(target-nums[i],i-1)
            
#             memo[(target,i)] = take or not_take
#             return memo[(target,i)]
        
#         summ= sum(nums)
#         return False if summ%2 else dp(summ//2,len(nums)-1)
        summ= sum(nums)
        n = len(nums)
        target = summ//2
        dp = [[False for _ in range(target+1)] for _ in range(n)]
        for i in range(n):
            dp[i][0] = True
    
    
        for i in range(n):
            for t in range(target+1):
                not_take =dp[i-1][t]       
                take = False
                if target-nums[i] >=0:
                    take = dp[i-1][t-nums[i]]
                
                dp[i][t] = take or not_take
        
        return  False if summ%2 else dp[-1][summ//2]