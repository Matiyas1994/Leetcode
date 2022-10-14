class Solution:

    #Function to find minimum time required to rot all oranges. 
	def orangesRotting(self, grid):
		#Code here
		from collections import deque
		
		pq = deque()
        n, m = len(grid), len(grid[0])
        visited = set()
        
        directions = [[-1,0],[1,0],[0,1],[0,-1]]
        inbound = lambda x,y: 0<=x<n and 0<=y<m and grid[x][y]==1
        countOranges = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    pq.append((i,j,0))
                    visited.add((i,j))
                if grid[i][j] !=0:
                    countOranges +=1
                    
        mx = float("-inf")                  
        while pq:
           
            
            
            for _ in range(len(pq)):
                
                i, j, time = pq.popleft()
                
                mx = max(time, mx)
                
                for d in directions:
                    ni , nj = i + d[0], j+d[1]
    
                    if inbound(ni, nj) and (ni, nj) not in visited:
                        pq.append((ni,nj,time+1))
                        visited.add((ni,nj))
                        
        return mx if len(visited) == countOranges else -1
                        
                
            
            

#{ 
 # Driver Code Starts
from queue import Queue

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = map(int, input().split())
		grid = []
		for _ in range(n):
			a = list(map(int, input().split()))
			grid.append(a)
		obj = Solution()
		ans = obj.orangesRotting(grid)
		print(ans)

# } Driver Code Ends