class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        elementIndex = {val:i for i,val in enumerate(nums)}
        
        for i in range(len(nums)):
            if target - nums[i] in elementIndex:
                if i != elementIndex[target - nums[i]]:
                    return[i,elementIndex[target - nums[i]]]
        
            
            
        