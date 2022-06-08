class Solution:
    def removePalindromeSub(self, s: str) -> int:
        return 1 if s==s[::-1] else 2  
        
        
#         p1 = 0
#         p2 = len(s)-1
#         c = 0
#         while p1 <= p2:
#             if s[p1] != s[p2]:
#                 c +=1
#             p1 +=1
#             p2 -=1
            
#         return c+1
            
        
        