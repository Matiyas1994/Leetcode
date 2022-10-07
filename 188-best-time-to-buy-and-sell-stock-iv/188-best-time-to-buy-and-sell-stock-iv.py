class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        @cache
        def f(i,canIbuy,k):
            if i==len(prices) or k == 0: return 0
            
            if canIbuy:
                profit = max(-prices[i]+f(i+1,0,k), f(i+1,1,k))
            
            else:
                profit = max(prices[i]+f(i+1,1,k-1), f(i+1,0,k))
            
            return profit
        
        return f(0,1,k)