class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        """
        Time-> O(2*N*M)
        Space-> O(1) 
        """
        m, n = len(matrix), len(matrix[0])
        colf = 1
        
        for i in range(m):
            if matrix[i][0] == 0:
                colf = 0
            for j in range(1,n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
            
            
        for i in range(m-1,-1,-1):
            for j in range(n-1,0,-1):
                if matrix[i][0] == 0 or matrix[0][j]==0:
                    matrix[i][j] = 0
            if colf == 0:
                matrix[i][0] = 0
        
       