class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        dp = [-1]*len(nums)
        
        def trav(idx):
            if nums[idx]==-1:
                return 0
            
            if dp[idx] !=-1:
                return dp[idx]
            
            t = nums[idx]
            nums[idx] = -1
            dp[idx] = trav(t) + 1
            nums[idx] = t
            return dp[idx]
        
        ans = 1
        for i in range(len(nums)):
            ans = max(ans, trav(i))  
            
        return ans
        #   0 1 2 3 4 5 6
        # [-1,4,-1,3,1,-1,-1]
          