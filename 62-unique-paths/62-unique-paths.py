class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
#         memo = {}
#         legitMove = lambda row , col : 0 <=row < m and 0<= col < n 
#         def pathCounter(r=0, c=0):
#             nonlocal m,n
#             if r == m-1 and c == n-1:
#                 return 1
#             if (r,c) not in memo:
#                 r1, r2 = 0, 0
#                 if legitMove(r+1,c):
#                     r1 =  pathCounter(r+1,c)
#                 if legitMove(r,c+1):
#                     r2 = pathCounter(r,c+1)
#                 memo[(r,c)] = r1 + r2 
            
#             return memo[(r,c)]
        
#         return pathCounter()

        dp = [[ 1 if i==0 or j==0 else 0  for i in range(n)] for j in range(m)]
        
        for r in range(1,m):
            for c in range(1,n):
                dp[r][c] = dp[r-1][c] + dp[r][c-1]
        
        return dp[m-1][n-1]
        