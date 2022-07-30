class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def valid(r,c,num):
            
            for i in range(9):
                if num == board[i][c]:
                    return False
                if num == board[r][i]:
                    return False
                
           
            SubrowStart = 3*(r//3)
            SubcolStart = 3*(c//3)
            for i in range(SubrowStart, SubrowStart +3):
                for j in range(SubcolStart, SubcolStart+3):
                    if board[i][j] == num:
                        return False
                  
            return True
                    
        
        def sudukusolver():
            
            for r in range(9):
                for c in range(9):
                    if board[r][c] == ".":
                        for num in range(1,10):
                            if valid(r, c, str(num)):
                                board[r][c] = str(num)
                                if sudukusolver(): 
                                    return True
                                else: 
                                    board[r][c] = "."
                        return False
            return True
                            
        sudukusolver()
           
    