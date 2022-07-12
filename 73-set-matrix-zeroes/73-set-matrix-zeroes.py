class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        def make_row_zero(r):
            for i in range(0,n):
                matrix[r][i] = 0
        def make_col_zero(c):
            for j in range(0,m):
                matrix[j][c] = 0
            
        sbz=[]
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    sbz.append((i,j))
        for tup in sbz:
            make_row_zero(tup[0])
            make_col_zero(tup[1])