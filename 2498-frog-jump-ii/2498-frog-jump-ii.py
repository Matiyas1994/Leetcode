class Solution:
    def maxJump(self, s: List[int]) -> int:
        m = s[1]
        for i,j in zip(s[2:],s):
            m = max(m, i-j)
        return m
#         maxJump = 0
#         n = len(stones) 
#         if n<3: return stones[1]-stones[0]
        
#         for i in range(0,n-1,2):
#             maxJump = max(maxJump, abs(stones[i]- stones[i+2]))
#         maxJump = max(maxJump, abs(stones[-1]- stones[-2]))
#         for i in range(n-2, 1, -2):
#             maxJump = max(maxJump, abs(stones[i]-stones[i-2]))
#         maxJump = max(maxJump, abs(stones[1]- stones[0]))
#         return maxJump
          