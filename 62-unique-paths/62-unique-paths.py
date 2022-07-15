class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        reqSteps = m+n-2
        r = m-1
        numerator = 1
        denominator = 1
        return comb(reqSteps,r) 
        """
        comination  c(reqSteps, r) , my combination implimentation
        """
#         for i in range(1,r+1):
#             numerator *= (reqSteps - r + i)
#             denominator *= i
        
#         return numerator//denominator
        
        
        
        
        
#         dp=[[0 for _ in range(n)] for _ in range(m)]
#         for i in range(m):
#             dp[i][0] = 1
#         for j in range(n):
#             dp[0][j] = 1
        
#         for i in range(1,m):
#             for j in range(1,n):
#                 dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
#         return dp[m-1][n-1]
        
        
        
        