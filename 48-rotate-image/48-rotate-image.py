class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        """
        Clocwise = reverse Matrix(top to down) + transponse
        anticlockWise = reverse Matrix(each row left to right) + transponse
        """
        def clockwise():
            matrix.reverse()
            transponse()
        def antiClockwise():
            for r in matrix:
                r.reverse()
            transponse()
        
        def transponse():
            for i in range(len(matrix)):
                for j in range(i+1, len(matrix)):
                    matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
        
        clockwise()
        
        
        
        
        # def reverse():
        #     for r in range(len(matrix)):
        #         s = 0
        #         e = len(matrix)-1
        #         while s < e:
        #             matrix[r][s], matrix[r][e] = matrix[r][e], matrix[r][s]
        #             s +=1
        #             e -=1
        
        
        
            
        