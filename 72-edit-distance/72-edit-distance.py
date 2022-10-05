class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1, l2 = len(word1), len(word2)
        
        dp = [[0 for _ in range(l2+1)] for _ in range(l1+1)]
        
        for j in range(l2+1):
            dp[0][j] = j
        
        for i in range(l1+1):
            dp[i][0] = i
        
        for i in range(1, l1+1):
            for j in range(1, l2+1):
                
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                    
                else:
                    insert = dp[i][j-1] + 1
                    delete = dp[i-1][j] + 1
                    replace = dp[i-1][j-1] + 1
                    
                    dp[i][j] = min(insert, delete, replace) 
                    
       
        return dp[l1][l2]

               

        
       
#         memo = {}
        
#         def f(i, j):
#             if i < 0: return j+1
#             if j < 0: return i+1
            
#             if (i, j) in memo:
#                 return memo[(i,j)]
            
#             if word1[i] == word2[j]:
#                 memo[(i,j)] = f(i-1, j-1) 
#             else:
#                 insert = f(i, j-1) + 1
#                 delete = f(i-1, j) + 1
#                 replace = f(i-1, j-1) + 1
                
#                 memo[(i,j)] = min(insert, delete, replace)
            
#             return memo[(i, j)]
        
        
        
#         return  f(l1-1, l2-1)
        