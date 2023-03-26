class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def valid(board, number, row, col):
            
            #row wise and column wise check
            for i in range(9):
                if board[row][i]==number or board[i][col] == number:
                    return False
                
            startOfRow = (row//3)*3 
            startOfCol = (col//3)*3 
            
            for i in range(startOfRow, startOfRow+3):
                for j in range(startOfCol, startOfCol+3):
                    if board[i][j]== number:
                        return False
            
            return True
            
        

        for row in range(9):
            for col in range(9):
                if board[row][col]==".":
                    for num in range(1, 10):
                        if valid(board, str(num),row, col):
                            board[row][col] = str(num)
                            if self.solveSudoku(board):
                                return True
                            board[row][col] = "."
                            
                    return False
                
        return True
        
                    
                   
                
                
#     [["5",".","4","6","7","8","9","1","2"],
#      ["6","7","2","1","9","5","3","4","8"],
#      ["1","9","8","3","4","2","5","6","7"],
#      ["8","5","9","7","6","1","4","2","3"]
#      ["4","2","6","8","5","3","7","9","1"],
#      ["7","3",".","9","2","4","8","5","6"],
#      ["9","6","1","5","3","7","2","8","4"],
#      ["2","8","7","4","1","9","6","3","5"],
#      ["3","4","5","2","8","6","1","7","9"]]                        
                            
                            

                        
# [["5","3","1","2","7","4","6",".","."],
#  ["6",".",".","1","9","5",".",".","."],
#  [".","9","8",".",".",".",".","6","."],
#  ["8",".",".",".","6",".",".",".","3"],
#  ["4",".",".","8",".","3",".",".","1"],
#  ["7",".",".",".","2",".",".",".","6"],
#  [".","6",".",".",".",".","2","8","."],
#  [".",".",".","4","1","9",".",".","5"],
#  [".",".",".",".","8",".",".","7","9"]]
       
        