class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.dp = [[0 for i in range(len(matrix[0])+1)] 
                   for j in range(len(matrix)+1)]
        
        # Buiiding comulative sum relative to the orgin for each cell
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                self.dp[r+1][c+1] = (self.matrix[r][c]
                                     +self.dp[r][c+1]
                                     +self.dp[r+1][c]
                                     -self.dp[r][c])
    
    
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        dp = self.dp
        
        return (dp[row2+1][col2+1] - dp[row2+1][col1]
                - dp[row1][col2+1] + dp[row1][col1]) 

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

