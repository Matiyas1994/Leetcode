class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        mn = nums[0]
        ans = -1
        
        for i in range(1,len(nums)):
            if nums[i] <= mn:
                mn = nums[i]
            else:
                ans = max(ans, nums[i]-mn)
        
        return ans
            
        