class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle =="":
            return 0
        
        Nh, Nn = len(haystack), len(needle)
        
        for i in range(Nh-Nn+1):  
            if haystack[i] == needle[0]:
                if haystack[i:].startswith(needle):
                    return i
        return -1
        
        
        # if needle in haystack:
        #     return haystack.index(needle)
        # return -1
    
        