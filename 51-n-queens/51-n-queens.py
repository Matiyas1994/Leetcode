class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        colset = set()
        leftdiagonal = set()
        rightdiagonal = set()  
        board = [['.' for _ in range(n)]for _ in range(n)]
      
        def valid(r,c):
            return ( 
                    c not in colset
                    and r+c not in rightdiagonal
                    and c-r not in leftdiagonal
                    )
        
        def backtrack(rs, board):
            nonlocal n
            if rs == n:
                temp = []
                for row in board:
                    temp.append("".join(row))
                ans.append(temp)
            
            else:
                for c in range(n):
                        if valid(rs,c):
                            board[rs][c] = 'Q'
                            colset.add(c)
                            rightdiagonal.add(rs+c)
                            leftdiagonal.add(c-rs)
                            
                            backtrack(rs+1, board)
                            
                            board[rs][c] = '.'
                            colset.remove(c)
                            rightdiagonal.remove(rs+c)
                            leftdiagonal.remove(c-rs)
                            
        backtrack(0, board)
        return ans
        
                            
                            