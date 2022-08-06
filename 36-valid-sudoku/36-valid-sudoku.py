class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        submatrix = [set() for _ in range(9)]
        rowset = [set() for _ in range(9)]
        colset = [set()for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                if board[i][j] !=".":
                    if board[i][j] in rowset[i]:
                        return False
                    rowset[i].add(board[i][j])

                    if board[i][j] in colset[j]:
                        return False
                    colset[j].add(board[i][j])
                    
                    if board[i][j] in  submatrix[(3*(i//3))+(j//3)]:
                        return False
                    submatrix[(3*(i//3))+(j//3)].add(board[i][j])
                               
        return True
        
        
#         def validator(r, c):
#             for i in range(9):
#                 if i!=r and board[i][c]==board[r][c]:
#                     return False 
#                 if i!=c and board[r][i] ==board[r][c]:
#                     return False
            
#             sr = 3*(r//3)
#             sc = 3*(c//3)
            
#             for i in range(sr,sr+3):
#                 for j in range(sc,sc+3):
#                     if i!=r and j!=c and board[i][j] == board[r][c]:
#                         return False
            
#             return True
        
#         for i in range(9):
#             for j in range(9):
#                 if board[i][j] != ".":
#                     if not validator(i, j):
#                         return False
#         return True
            
            