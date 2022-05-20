class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0
        
        memo = [[0 for i in range(n)] for j in range(m)]
 
        memo[0][0] = 1
        
        
        def validmove(i,j):
            nonlocal m,n
            if 0 <= i < m and 0 <= j < n:
                if obstacleGrid[i][j] == 0:
                    return True
                return False
            return False
        
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if validmove(i,j+1):
                    memo[i][j+1] +=memo[i][j]
                if validmove(i+1,j):
                    memo[i+1][j] +=memo[i][j]
        return memo[m-1][n-1]
                
                    
        
        
        
        
        
        
        
        
        
        
#         ans = 0
#         m, n = len( obstacleGrid), len( obstacleGrid[0])
#         if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
#             return 0
#         def validmove(vertex):
#             nonlocal m,n
#             if 0 <= vertex[0] < m and 0 <= vertex[1] < n:
#                 if obstacleGrid[vertex[0]][vertex[1]] == 0:
#                     return True
#                 return False
#             return False
        
        
#         def dfs(start):
#             nonlocal ans,m ,n
#             if start[0]== m-1 and start[1]==n-1:
#                 ans +=1
#                 return
            
#             if validmove((start[0],start[1]+1)):
#                 dfs((start[0],start[1]+1))
#             if validmove((start[0]+1,start[1])):
#                 dfs((start[0]+1,start[1]))
#         dfs((0,0))
#         return ans