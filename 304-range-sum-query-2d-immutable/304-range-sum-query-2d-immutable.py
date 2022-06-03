class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.prefix_matrix = []
        
        # PreProcessing the matrix by building prefix sum         
        for i in range(len(matrix)):
            temp = [0]
            for j in range(len(matrix[0])):
                temp.append(matrix[i][j] + temp[-1])
                
            self.prefix_matrix.append(temp)
        
    
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum_of_bounded_region = 0
        for i in range(row1,row2+1):
            sum_of_bounded_region += (self.prefix_matrix[i][col2+1]
                                      -self.prefix_matrix[i][col1])
                
        return sum_of_bounded_region

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)