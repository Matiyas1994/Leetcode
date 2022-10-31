class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        prefix1 = [0]*n
        prefix2 = [0]*n
        j = n-1
        prefix1[0] = grid[0][0]
        for i in range(1, n):
            prefix1[i] = prefix1[i-1]+grid[0][i]
            
        prefix2[-1] = grid[1][-1]
        for j in range(n-2,-1,-1):
            prefix2[j] = prefix2[j+1]+grid[1][j]

        
        mn = float("inf")
        for i in range(n):
            mn = min(mn, max(prefix1[-1]-prefix1[i], prefix2[0]-prefix2[i]))
        return mn
        
        
            
        