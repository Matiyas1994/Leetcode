class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        
        dp = [0 for _ in range(m+1)]
        dp[0] = 1

              
        for i in range(1, n+1):
               for j in range(m,0,-1):
                    
                    if s[i-1]==t[j-1]:
                        dp[j] += dp[j-1] 
               
                    else:
                        dp[j] = dp[j]
               
        return dp[m]
               