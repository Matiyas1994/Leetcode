class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        n, m = len(mat), len(mat[0])
        ans = [[0 for _ in range(m)] for _ in range(n)]
         
        visited= set()
        inbound = lambda x,y: 0<=x<n and 0<=y<m
#                     down   up    right  left
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        queue= deque()  
        
        def bfs():         
            
            while queue:
                i, j, val = queue.popleft()
                ans[i][j] = val 
                
                for d in directions:
                    ni, nj = i+d[0], j+d[1]
                    
                    if inbound(ni,nj) and (ni, nj) not in visited:
                        visited.add((ni,nj))
                        queue.append((ni, nj, val+1))
                        
                    
        for i in range(n):
            for j in range(m):
                if mat[i][j]==0:
                    queue.append((i, j, 0))
                    visited.add((i, j))
        bfs()
        return ans
                
    
            