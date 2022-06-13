class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        if n == 1:
            return matrix[0][0]
        
        valid = lambda i,j: 0<= i < n and 0<= j < n 
        
        dp = [[ 0 for i in range(n)] for j in range(n)]
        for i in range(n):
            dp[n-1][i] = matrix[n-1][i]
        
        for r in range(n-2,-1,-1):
            for c in range(n):
                d = dp[r+1][c] if valid(r+1,c) else float(inf)
                ld = dp[r+1][c-1] if valid(r+1,c-1) else float(inf)
                rd = dp [r+1][c+1] if valid(r+1,c+1) else float(inf)
                dp [r][c] = min(d,ld,rd) + matrix[r][c]
        
        return min(dp[0])
        
        
        
        
        
        
#         memo = {}
#         def dp (r,c):
#             if r >= n:
#                 return 0
#             if (r,c) in memo:
#                 return memo[(r,c)]
            
#             d =
#             rd =
#             ld =
            
#             memo[(r,c)] = min(d,rd,ld) + matrix[i][j]
            
#             return memo[(r,c)]
            
        
        
#         return dp(0,0)