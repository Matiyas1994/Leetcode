class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}

        def dp(i):
            if i in memo:
                return memo[i]

            max_length = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    max_length = max(max_length, memo[j] + 1)

            memo[i] = max_length
            return max_length

        max_length = 1
        for i in range(n):
            max_length = max(max_length, dp(i))

        return max_length



        
        
#         def firstGreatorElement(ds, targ):
#             left, right = 0, len(ds)-1
#             candidate = right
#             while left<=right:
#                 mid = left + (right-left)//2
                
#                 if ds[mid] >= targ:
#                     candidate = mid
#                     right = mid-1
#                 else:
#                     left = mid+1
            
#             return candidate
#         ds = [nums[0]]
#         for i in range(1, len(nums)):
#             if nums[i] > ds[-1]:
#                 ds.append(nums[i])
#             else:
#                 idx = firstGreatorElement(ds, nums[i])
#                 ds[idx] = nums[i]

        
#         return len(ds)
                
            
            
            
        
        
        
        
        
        
        
#         dp = [ 1 for i in range(len(nums))]
#         ans = 1
        
#         for i in range(1, len(nums)):
#             for j in range(i-1, -1,-1):
#                 if nums[j] < nums[i]:
#                     dp[i] = max(dp[j]+1, dp[i])
#             ans = max(ans, dp[i])

#         return ans
        
        