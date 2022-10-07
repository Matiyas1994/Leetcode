class Solution:
    def maxProfit(self, prices: List[int]) -> int:   
#         memo={}
#         def f(i, canIbuy):
#             if i==len(prices):
#                 return 0
#             if (i, canIbuy) in memo:
#                 return memo[(i,canIbuy)]
#             if canIbuy:
#                 profit = max(-prices[i]+ f(i+1, False), f(i+1, True))
                
#             else:
#                 profit = max(prices[i]+f(i+1, True), f(i+1, False))
            
#             memo[(i, canIbuy)] = profit
#             return memo[(i, canIbuy)] 
#         return f(0,True)
   

        dp = [[0 for j in range(len(prices)+1)] for i in range(2)]
    
        for i in range(len(prices)-1,-1,-1):
            for canIbuy in [0, 1]:
                if canIbuy:
                    dp[canIbuy][i] = max(-prices[i]+dp[0][i+1], dp[1][i+1])
                else:
                    dp[canIbuy][i] = max(prices[i]+dp[1][i+1], dp[0][i+1])
                
        return dp[1][0]
        
            
            