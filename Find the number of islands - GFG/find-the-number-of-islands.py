#User function Template for python3

import sys
sys.setrecursionlimit(10**8)
class Solution:
    def numIslands(self,grid):
        #code here
        n ,m= len(grid), len(grid[0])
        dire = [[1,0],[0,1],[-1,0],[0,-1],[-1,-1],[1,-1],[-1,1],[1,1]]
        inbound = lambda x,y: 0<=x<n and 0<=y<m
        def go(i,j):
            if grid[i][j]==0: return
            grid[i][j]=0
            
            for d in dire:
                ni, nj= i+d[0], j+d[1]
                if inbound(ni,nj):
                    go(ni,nj)
        
        islands = 0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    go(i,j)
                    islands +=1
        return islands
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n,m=map(int,input().strip().split())
        grid=[]
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        obj=Solution()
        print(obj.numIslands(grid))
# } Driver Code Ends