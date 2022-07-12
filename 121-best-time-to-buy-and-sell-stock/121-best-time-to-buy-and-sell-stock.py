class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_so_far = []
        for i,n in enumerate(prices):
            heapq.heappush(max_so_far,(-1*n,i))
        
        max_profit = 0
        for i in range(len(prices)-1):
            while max_so_far[0][1] <= i:
                heapq.heappop(max_so_far)
            max_profit = max(max_profit, -1*max_so_far[0][0] - prices[i])
        
        return max_profit
        
        