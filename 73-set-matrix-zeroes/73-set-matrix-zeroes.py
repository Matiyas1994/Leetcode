class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        def make_row_zero(r):
            for i in range(0,n):
                if matrix[r][i] !=0:
                    matrix[r][i] = "c"
        def make_col_zero(c):
            for j in range(0,m):
                if matrix[j][c] !=0:
                    matrix[j][c] = "c"
            
    
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    make_row_zero(i)
                    make_col_zero(j)
                    
        for i in range(m):
            for j in range(n):
                if matrix[i][j]=="c":
                    matrix[i][j] = 0
                
       