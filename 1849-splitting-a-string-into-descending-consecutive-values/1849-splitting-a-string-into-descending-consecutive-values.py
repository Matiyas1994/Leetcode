class Solution:
    def splitString(self, s: str) -> bool:
        
        def dfs(start, sofar):
            
            if start >= len(s) and len(sofar) > 1:
                return True
            
            for i in range(start, len(s)):
                current = int(s[start:i+1])
                if len(sofar)==0 or sofar[-1]-1==current:
                    sofar.append(current)
                    if dfs(i+1, sofar): return True
                    sofar.pop()
        
        return dfs(0, [])
            
        