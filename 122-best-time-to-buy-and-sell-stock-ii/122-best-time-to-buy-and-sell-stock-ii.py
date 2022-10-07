class Solution:
    def maxProfit(self, prices: List[int]) -> int:   
        memo={}
        def f(i, canIbuy):
            if i==len(prices):
                return 0
            if (i, canIbuy) in memo:
                return memo[(i,canIbuy)]
            if canIbuy:
                profit = max(-prices[i]+ f(i+1, False), f(i+1, True))
                
            else:
                profit = max(prices[i]+f(i+1, True), f(i+1, False))
            
            memo[(i, canIbuy)] = profit
            return memo[(i, canIbuy)] 
        return f(0,True)
        
        
            
            