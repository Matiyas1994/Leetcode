class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            if n == 1:
                return nums[0]
            return max(nums[0],nums[1])
        
        
        case1 = nums[0]
        case2 = max(nums[0],nums[1])
        
        for i in range(2,n):
            res = max(case1 + nums[i], case2)
            case1 = case2
            case2 = res
            
        return res
        
            
        
        