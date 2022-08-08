class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [ 1 for i in range(len(nums))]
        ans = 1
        
        for i in range(1, len(nums)):
            for j in range(i-1, -1,-1):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j]+1, dp[i])
            ans = max(ans, dp[i])
        print(dp)
        return ans
        
        