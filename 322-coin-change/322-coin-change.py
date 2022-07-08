class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp =[float("inf") for i in range(amount+1)]
        dp[0] = 0
        
        for i in range(amount+1):
            for c in coins:
                if i-c >=0:
                    dp[i] = min(dp[i-c] + 1, dp[i])
       
        return dp[-1] if dp[-1] < float("inf") else -1