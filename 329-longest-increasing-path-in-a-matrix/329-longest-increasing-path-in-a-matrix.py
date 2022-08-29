class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dir_ = [(1,0),(-1,0),(0,1),(0,-1)]
        dic = {}
        valid = lambda x, y:  0<= x < len(matrix) and 0<= y < len(matrix[0])
        
        def dfs(i,j, visited):
            if (i,j) in  dic:
                return dic[(i,j)]
            
            visited.add((i,j))
            cur = 0
            for r, c in dir_:
                ni = i+r  
                nj = j+c
                
                if ((ni, nj) not in visited 
                    and valid(ni,nj) 
                    and matrix[ni][nj] > matrix[i][j]):
                    
                    cur = max(dfs(ni, nj, visited), cur)
            visited.remove((i,j))
            dic[(i,j)] = cur + 1
            return dic[(i,j)] 
        
        ans = 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (i,j) not in dic:
                    ans = max(dfs(i,j, set()), ans)
                    
        return ans
                           
            
        