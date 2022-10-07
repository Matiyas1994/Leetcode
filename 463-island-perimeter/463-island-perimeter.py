class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        direc = [(0,1),(1,0),(-1,0),(0,-1)]
        n, m = len(grid), len(grid[0])
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    for d in direc:
                        ni, nj = i+d[0],  j+d[1]
                        if 0 <= ni < n and 0 <= nj < m:
                            ans += abs(grid[ni][nj]-1)
                        else:
                            ans +=1
        return ans
                    

                    