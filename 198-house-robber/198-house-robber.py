class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        first, last = nums[0], max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            last, first = max(last, first+nums[i]), last
      
        return last