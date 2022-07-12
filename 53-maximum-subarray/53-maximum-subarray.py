class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = nums[0]
        max_sum = nums[0]
        for i in range(1,n):
            dp = max(dp+nums[i], nums[i])
            max_sum = max(dp, max_sum)
        
        return max_sum