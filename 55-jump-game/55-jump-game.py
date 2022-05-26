class Solution:
    def canJump(self, nums: List[int]) -> bool:

        n = len(nums)
        dp = [False for _ in range(n)]
        dp[-1] = True
        lt = n-1
        for i in range(n-2,-1,-1):
            if nums[i] >= lt -i:
                dp[i] = True
                lt = i
        return dp[0]


#         if len(nums) == 1:
#             return True
#         memo = {}
#         def jump(idx = 0):
#             if idx >= len(nums)-1:
#                 memo[idx] = True
#                 return True
#             if idx in memo:
#                 return memo[idx]
            
#             for j in range(1,nums[idx]+1):
#                 if jump(idx + j):
#                     memo[idx] = True
#                     return True
#             memo[idx] = False
#             return memo[idx]
#         return jump()

    
        
        # [T,T,T,T,T]
        # [F,F,F,F,T]
        #  0 1 2 3 4
        # [        T]
        # 4-1 = 3
        # if nums[idx] >= last trueindx - idx:
        #     True