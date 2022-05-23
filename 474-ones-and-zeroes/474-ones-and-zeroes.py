class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        memo = {}
        def dp(i = 0, numOf1 = n, numOf0 = m):
            
            if numOf1 < 0  or numOf0 < 0 or i == len(strs):
                return 0
            if(i,numOf0,numOf1) in memo:
                return memo[(i,numOf0,numOf1)]
            
            n1 = strs[i].count("1") 
            n0 = len(strs[i]) - n1
            
            r1 = dp(i+1,numOf1,numOf0)
            r2 = 0
            if numOf1 - n1 >= 0 and numOf0 - n0 >= 0:
                r2 = dp(i + 1,numOf1 - n1, numOf0 - n0) + 1
            
            memo[(i,numOf0,numOf1)] = max(r1,r2)
            return memo[(i,numOf0,numOf1)]
        
        return dp()
    
        
            
        
        
#         def dp(i = 0, numOf1 = 0, numOf0 = 0):
#             nonlocal m , n
#             if numOf1 > n or numOf0 > m or i == len(strs):
#                 return 0
#             n1 = strs[i].count("1") 
#             n0 = len(strs[i]) - n1
            
#             return max(dp(i + 1,n1 + numOf1, n0 + numOf0), dp(i+1, numOf1,numOf0)) + 1
         
#         return dp()
        
        
        
        
        
        
        
#         ans = 0
#         numOf1 = 0
#         numOf0 = 0
#         for sub in sorted(strs,key=len):
#             for i in range(len(sub)):
#                 if sub[i]=="1":
#                     numOf1 +=1
#                 else:
#                     numOf0 +=1
                    
#                 if numOf0 > m or numOf1 > n:
#                     break
                    
#             if numOf0 <= m and numOf1 <= n:
#                 ans +=1
                
#         return ans