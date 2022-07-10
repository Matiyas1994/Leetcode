class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp =[0 for i  in range(n)]
        dp[0] = cost[0]
        dp[1] = cost[1]
        
        for i in range(2,n):
            dp[i] = min(dp[i-1],dp[i-2]) + cost[i]
        
        return min(dp[n-1],dp[n-2])
        
        
        
        
        
#         minimumCost = float(inf)
        
#         def dp(indx,c):
#             nonlocal minimumCost
            
#             if indx == len(cost):
#                 minimumCost = min(c,minimumCost)
#                 return 
            
#             dp(indx + 1, cost[indx] + c)
#             dp(indx + 2, cost[indx] + c)
            
#         dp(0,0)
#         dp(1,0)
        
#         return minimumCost
        
#         cache={}
#         cost.append(0)
#         def dp(index):
#             if index in cache:
#                 return cache[index]
   
#             if index < 2:
#                 return cost[index]
            
#             cache[index]= cost[index] + min(dp(index-1),dp(index-2))
            
#             return cache[index]
        
#         return dp(len(cost)-1)