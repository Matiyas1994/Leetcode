class Solution:
    def simplifyPath(self, path: str) -> str:
        pathlist = path.split("/")
        ans = []
        for p in pathlist:
            if p == "..":
                if ans:
                    ans.pop()
            elif p =="" or p==".":
                continue
            else:
                ans.append(p)
        
        return "/" + "/".join(ans)        
                
                
        
