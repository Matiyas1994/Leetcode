class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price_so_far = float(inf)
        
        for i in range(len(prices)):
            min_price_so_far = min(min_price_so_far, prices[i])
            max_profit = max(max_profit, prices[i] - min_price_so_far)
        
        return max_profit
        