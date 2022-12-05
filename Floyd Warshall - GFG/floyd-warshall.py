#User function template for Python

class Solution:
	def shortest_distance(self, matrix):
		#Code here
		n = len(matrix)
		for intermidiate in range(n):
		    for nodeA in range(n):
		        for nodeB in range(n):
		                if matrix[nodeA][intermidiate] !=-1 and matrix[intermidiate][nodeB] !=-1:
		                    cur = float('inf') if matrix[nodeA][nodeB] == -1 else matrix[nodeA][nodeB]
		                    matrix[nodeA][nodeB] = min(cur, matrix[nodeA][intermidiate] + matrix[intermidiate][nodeB] )
		      
        return matrix 

#{ 
 # Driver Code Starts
#Initial template for Python 

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		matrix = []
		for _ in range(n):
			matrix.append(list(map(int, input().split())))
		obj = Solution()
		obj.shortest_distance(matrix)
		for _ in range(n):
			for __ in range(n):
				print(matrix[_][__], end = " ")
			print()
# } Driver Code Ends