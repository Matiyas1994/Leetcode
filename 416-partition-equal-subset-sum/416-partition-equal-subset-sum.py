class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memo = {}
        def dp(target, i):
            if target==0:
                return True
            if i < 0:
                return False
            if (target,i) in memo:
                return memo[(target,i)]
            
            not_take = dp(target,i-1)
            if(not_take):
                return True
            take = False
            if target-nums[i] >=0:
                take = dp(target-nums[i],i-1)
            
            memo[(target,i)] = take or not_take
            return memo[(target,i)]
        
        summ= sum(nums)
        return False if summ%2 else dp(summ//2,len(nums)-1)