class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def f(i,canIbuy,n):
            if i==len(prices) or n==0: return 0
            
            if (i, canIbuy, n) in memo:
                return memo[(i, canIbuy, n)]
            
            if canIbuy:
                profit = max(-prices[i]+f(i+1,0,n), f(i+1,1,n))
                
            else:
                profit = max(prices[i]+f(i+1,1,n-1), f(i+1,0,n))
            
            memo[(i, canIbuy, n)] = profit
            return memo[(i, canIbuy, n)]
        
        return f(0,1,2)
        