class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        dp = [[0]*len(s) for i in range(len(s))]
        
        for i in range(len(s)):
            dp[i][i] = True
            res = s[i]
			
        for i in range(len(s)-1,-1,-1):
            for j in range(i+1,len(s)):  
                
                if s[i] == s[j]:
                    if j-i ==1 or dp[i+1][j-1] is True:
                        dp[i][j] = True
                        
                        if len(res) < len(s[i:j+1]):
                            res = s[i:j+1]
                
        return res
        
        
#         n = len(s)
#         dp = []
#         for i in range(n):
#             li = []
#             for j in range(n):
#                 if i == j:
#                     li.append(1)
#                 else:
#                     li.append(0)
#             dp.append(li)
            
#         st, e, i, j = 0,  1, 0, 1
#         while j < n:
#             if s[i] == s[j]:
#                 dp[i][j] = 1
#                 st, e = i, j + 1
#             i, j = i+1 , j+1
        
        
        
    
#         for k in range(2,n):
#             i, j = 0 , k
#             while j < n:
#                 if s[i]==s[j] and dp[i+1][j-1] == 1:
#                     dp[i][j] = 1
#                     st, e = i, j + 1
#                 i, j = i+1 , j+1
                
                
#         return s[st:e]
        
        
        
#         def ispal(st,e):
#             while st <= e:
#                 if s[st] != s[e]:
#                     return False
#                 st +=1
#                 e -=1
#             return True
        
        
#         memo = {}
#         def dp(st = 0,e = len(s)-1):
#             if ispal(st,e):
#                 memo[(st,e)] = (st,e)
#                 return (st,e)
#             if (st,e) in memo:
#                 return memo[(st,e)]
             
#             r1 = dp(st+1,e)
#             r2 = dp(st,e-1)
            
#             if (r1[1]-r1[0]) >= (r2[1]-r2[0]): 
#                 memo[(st,e)] = r1
#             else:
#                 memo[(st,e)] = r2
#             return memo[(st,e)]
        
#         res = dp()
#         return s[res[0]:res[1]+1]
        
            
            
        