class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        ans = 0 
        nums.sort()
        @lru_cache(None)
        def dfs(tar):
            if tar < 0:
                return 0
            if tar == 0:
                return 1
            ans = 0
            for i in range(len(nums)):
                if nums[i] <= tar:
                    ans += dfs(tar-nums[i])
                else:
                    break
            return ans
        return dfs(target)
#         def backtrack(sum_so_far):
#             nonlocal ans, target
#             if sum_so_far==target:
#                 ans +=1
            
#             else:
#                 for i in range(len(nums)):
#                     if nums[i] + sum_so_far <= target:
#                         backtrack(nums[i] + sum_so_far)
#                     else: 
#                         break
#         backtrack(0)
#         return ans
      
        
            
            