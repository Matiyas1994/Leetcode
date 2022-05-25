class Solution:
    def tribonacci(self, n: int) -> int:
        
#         memo = {}
#         def dp(n):
#             if n == 0:
#                 return 0
#             elif n < 3:
#                 return 1
#             if n  in memo:
#                 return memo[n]
            
#             memo[n] = dp(n-1) + dp(n-2) + dp(n-3)
#             return memo[n]
        
#         return dp(n)
        
        
        if n == 0:
            return 0
        if n < 3:
            return 1
        
        dp = [0 for _ in range(n+2)]
        dp[1] = 1
        dp[2] = 1
        
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
            
        return dp[n]