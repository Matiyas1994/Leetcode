class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        memo = {}
        
        def f(i, j):
            if j < 0: return  i < 0
            if i < 0:
                for k in range(j+1):
                    if p[k] != "*":
                        return False
                
                return True

            if (i,j) in memo:
                return memo[(i,j)]
            
            if s[i] == p[j] or p[j]=="?":
                memo[(i,j)] = f(i-1, j-1)

            elif p[j] == "*":
                
                memo[(i,j)] = f(i, j-1) or f(i-1, j)
                
            else:
                memo[(i,j)] = False
            
            return memo[(i,j)]
        
        return f(n-1, m-1)

        