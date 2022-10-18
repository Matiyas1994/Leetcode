class Solution:
        def isValidMove(self,x, y, grid):
            n = len(grid)
            return 0<=x<n and 0<=y<n and grid[x][y]==0
            
        def bfs(self,si, sj, move, grid):
                        # down   up    left   right  dl      dr    ur      ul     
            directions = [[1,0],[-1,0],[0,-1],[0,1],[1,-1],[1,1],[-1,1],[-1,-1]]
            queue = deque()
            visited = set()
            n = len(grid)
            
            queue.append((si, sj, move))
            visited.add((si,sj))
            
            while queue:
                current_i, current_j, move = queue.popleft()
                
                if current_i == n-1 and current_j == n-1:
                    return move
                
                for row, col in directions:
                    new_row, new_col = current_i+row, current_j+col
                    
                    if (new_row, new_col) not in visited and self.isValidMove(new_row, new_col, grid):
                        visited.add((new_row, new_col))
                        queue.append((new_row, new_col, move+1))
            
                    
            return -1    
        
    
        def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
            return self.bfs(0, 0, 1, grid) if grid[0][0]==0 else -1
