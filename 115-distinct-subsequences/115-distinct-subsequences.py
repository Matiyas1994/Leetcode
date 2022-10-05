class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        memo = {}
        def f(i, j):
            if j < 0: return 1
            
            if i < 0: return 0
            
    
            if (i,j) in memo:
                return memo[(i, j)]
            
            if s[i]==t[j]:
                memo[(i, j)] = f(i-1, j-1) + f(i-1, j)
            
            else:
                memo[(i, j)] = f(i-1, j)
            
            return memo[(i, j)]
        
        i, j = len(s)-1, len(t)-1
        return f(i, j)
            
        