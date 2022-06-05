class Solution:
    def totalNQueens(self, n: int) -> int:
        ans = 0
        col = set()
        PosDiagonal = set()
        negativeDiagonal = set()
        
        
        def quenPosition(r):
            nonlocal ans
            if r == n:
                ans +=1
                return 
            
            for c in range(n):
                if (c not in col and
                    r+c not in PosDiagonal and
                    r-c not in negativeDiagonal):
                    
                    col.add(c)
                    PosDiagonal.add(r+c)
                    negativeDiagonal.add(r-c)
                    
                    quenPosition(r+1)
                    
                    col.remove(c)
                    PosDiagonal.remove(r+c)
                    negativeDiagonal.remove(r-c)
            
        quenPosition(0)
        return ans
                    
                
               