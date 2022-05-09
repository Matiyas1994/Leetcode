class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle =="":
            return 0
        
        if needle in haystack:
            return haystack.index(needle)
        return -1
    
#         p1 = 0
#         p2 = len(needle)
        
#         while p2 < len(needle):
#             if haystack[p1:p2+1] == needle:
#                 return p1
#             p1 +=1
#             p2 +=1
            
#         return -1
        
        