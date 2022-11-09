class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = set()
        
        def f(s,start):
            ans.add(s)
            
            for i in range(start, len(s)):
                ns = s
                if not s[i].isdigit():
                    if s[i].isupper():
                        ns = s[:i] + s[i].lower() + s[i+1:]
                    else:
                        ns = s[:i] + s[i].upper() + s[i+1:]
                f(ns, i+1)
        f(s, 0)
        return list(ans)
            
                    
        
        