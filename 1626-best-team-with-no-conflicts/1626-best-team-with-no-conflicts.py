class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        included = set()
        memo = {}
        zipped = list(zip(scores, ages))
        zipped.sort(key= lambda x:(x[0],x[1]))
        dp = [0]*(len(zipped))
        dp[0] = zipped[0][0]
        for i in range(1,len(zipped)):
            dp[i] = zipped[i][0]
            for j in range(i):
                if zipped[i][1]>=zipped[j][1]:
                    dp[i] = max(dp[i] , dp[j] + zipped[i][0])
        return max(dp)
    
    
#         def dp(node, prevIncludedIdx):
#             if node >= len(scores):
#                 return 0
            
#             if (node, prevIncludedIdx+1) in memo:
#                 return memo[(node, prevIncludedIdx+1)]
            
#             include = 0
            
#             if prevIncludedIdx == -1 or  zipped[prevIncludedIdx][0] == zipped[node][0] or zipped[prevIncludedIdx][1] >= zipped[node][1]: 
#                 include = dp(node+1, node) + zipped[node][1]
             
#             leavehim = dp(node+1, prevIncludedIdx) 
            
#             memo[(node, prevIncludedIdx+1)] = max(include, leavehim)
#             return memo[(node, prevIncludedIdx+1)]
        
#         return dp(0, -1)
        