class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        _dir = [(1,0), (0,1), (-1,0), (0,-1)]
        inBound =  lambda x, y: 0 <= x < len(board) and 0 <= y < len(board[0])
        # visited = set()
        
        def dfs(i, j, idx, visited):
            if idx == len(word):
                return True
            
            visited.add((i,j))
            for pair in _dir:
                ni, nj = i + pair[0], j + pair[1]
                
                if ((ni, nj) not in visited
                    and inBound(ni, nj)
                    and word[idx]==board[ni][nj]):
              
                    if dfs(ni, nj, idx+1, visited): return True
            visited.remove((i, j))
                    
            
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if word[0] == board[i][j] and dfs(i,j, 1, set()):
                    return True
        
        return False
        
        