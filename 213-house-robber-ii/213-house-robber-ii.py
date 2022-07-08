class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 4:
            return max(nums)
            
        def ansGiver(arr):
            n = len(arr)
            dp = [0 for i in range(n)]
            dp[0] = arr[0]
            dp[1] = max(arr[1], arr[0])
            
            for i in range(2,n):
                dp[i] = max(dp[i-2]+arr[i], dp[i-1])
                
            return dp[-1]
            
        return max(ansGiver(nums[:len(nums)-1]),ansGiver(nums[1:]))
            
        