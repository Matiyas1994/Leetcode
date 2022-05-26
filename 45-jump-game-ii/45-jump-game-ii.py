class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = {}
        def minijump(idx = 0):
            if idx >= len(nums)-1:
                return 0
            if idx in memo:
                return memo[idx]
            res = float(inf)
            for i in range(1,nums[idx]+1):
                res = min(minijump(idx + i),res)
            memo[idx] =  res + 1
            return memo[idx]
        
        return minijump()
        