class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
        
        for i in range(n):
            for j in range(m):
                if word1[i] == word2[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i][j+1],dp[i+1][j])
    
        
        return n+m - 2*dp[-1][-1]