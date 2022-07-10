class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        case1 = cost[0]
        case2 = cost[1]
        res = case2
        
        for i in range(2,n):
            res = min(case2,case1) + cost[i]
            case1 = case2
            case2 = res
            
        return min(res,case1)
        
        
        
        
        
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