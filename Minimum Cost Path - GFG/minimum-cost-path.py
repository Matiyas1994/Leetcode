import heapq
class Solution:
    
    #Function to return the minimum cost to react at bottom
	#right cell from top left cell.
	def isInsideGrid(self, grid, i, j):
	    RowLength, ColLength = len(grid), len(grid)
	    return 0 <= i < RowLength and 0 <= j < ColLength
	def minimumCostPath(self, grid):
		#Code here
		rowLength, colLength = len(grid), len(grid[0])
		pq = []
		pq.append((grid[0][0], 0, 0))
		distance = [ [float('inf') for _ in range(colLength)] for _ in range(rowLength)]
		distance [0][0] = grid[0][0]
		directions = [(-1,0),(1,0),(0,1),(0,-1)]
	
		
		while pq:
		    distanceFromStartCell, i, j = heapq.heappop(pq) 

		    if i==rowLength-1 and j==colLength-1:
		        return  distanceFromStartCell
		   
		    for dx, dy in directions:
		        newRow, newCol = i+dx, j+dy
		        
		        if (self.isInsideGrid(grid, newRow, newCol)
		            and distanceFromStartCell + grid[newRow][newCol] < distance[newRow][newCol]):
		                updatedDistance = distanceFromStartCell + grid[newRow][newCol] 
		                heapq.heappush(pq, (updatedDistance, newRow, newCol))
		                distance[newRow][newCol] = updatedDistance
		 
		return distance[rowLength-1][colLength-1]
		        
		    
		
		
		
		


#{ 
 # Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		grid = []
		for _ in range(n):
			a = list(map(int, input().split()))
			grid.append(a)
		obj = Solution()
		ans = obj.minimumCostPath(grid)
		print(ans)

# } Driver Code Ends