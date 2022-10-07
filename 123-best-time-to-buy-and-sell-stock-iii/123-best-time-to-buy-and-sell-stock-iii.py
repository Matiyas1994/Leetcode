class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #  t       f
        # 1 2     1 2
        
        ast1, ast2, asf1, asf2 = 0,0,0,0
        for i in range(len(prices)-1,-1,-1):
            for canIbuy in range(2):
                for n in range(1,3):
                     if canIbuy:
                        if n==1: 
                            ast1 = max(-prices[i]+asf1, ast1)
                        else:
                            ast2 = max(-prices[i]+ asf2, ast2)
                            
                     else:
                        if n ==1:
                            asf1 = max(prices[i], asf1)
                        else:
                            asf2 = max(prices[i]+ast1, asf2)
                        
        return ast2            
        
#         memo = {}
#         def f(i,canIbuy,n):
#             if i==len(prices) or n==0: return 0
            
#             if (i, canIbuy, n) in memo:
#                 return memo[(i, canIbuy, n)]
            
#             if canIbuy:
#                 profit = max(-prices[i]+f(i+1,0,n), f(i+1,1,n))
                
#             else:
#                 profit = max(prices[i]+f(i+1,1,n-1), f(i+1,0,n))
            
#             memo[(i, canIbuy, n)] = profit
#             return memo[(i, canIbuy, n)]
        
#         return f(0,1,2)
        