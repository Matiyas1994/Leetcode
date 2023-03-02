class Solution:
    def numTrees(self, n: int) -> int:
        dp  = {0:1, 1:1, 2:2}
        for i in range(1, n+1):
            ans = 0
            for j in range(1,i+1):
                ans += dp[j-1] * dp[i-j] 
            dp[i] = ans
            
            
        return ans
            
        
        