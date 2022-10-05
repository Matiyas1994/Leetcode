class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        prefix = [0]
        n , ans = len(cardPoints), 0
        
        for i in range(n):
            prefix.append(prefix[-1] + cardPoints[i])
       

        for i in range(k+1):
            ans = max(ans, prefix[k-i] + (prefix[-1] - prefix[n-i]))
                      
        return ans

        
   
#         memo = {}
#         def dp(i,j):
#             nonlocal k
#             if i + (len(cardPoints)-(j+1)) == k:
#                 return 0
#             if (i,j) in memo:
#                 return memo[(i,j)]
#             l = dp(i+1,j) + cardPoints[i]
#             r = dp(i,j-1) + cardPoints[j]
            
#             memo[(i,j)] = max(l,r)
#             return memo[(i,j)]
       
        
#         return dp(0,len(cardPoints)-1)