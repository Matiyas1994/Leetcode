class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        [["1","1","1","1","0"],
         ["1","1","1","1","0"],
         ["1","1","1","1","1"],
         ["1","1","1","1","1"],
         ["0","0","1","1","1"]]
        """
        time -> O(M*N)
        space -> O(1)
        """
        row  = len(matrix)
        col  = len(matrix[0])
        max_len = 0
        new_matrix = [[ 0 for j in range(col+1)] for i in range(row+1)]
        
        for i in range(1, row+1):
            for j in range(1, col+1):
                if matrix[i-1][j-1] == "1":   
                    new_matrix[i][j] = min(new_matrix[i-1][j],
                                          new_matrix[i][j-1],
                                          new_matrix[i-1][j-1]) + 1
                    max_len = max(new_matrix[i][j], max_len)
            
        return max_len*max_len
                    
       