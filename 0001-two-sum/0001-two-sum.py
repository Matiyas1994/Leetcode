class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        elementWithIdx = {}
        
        for idx, number in enumerate(nums):
            if (target - number) in elementWithIdx:
                return[idx, elementWithIdx[target - number]]
            
            elementWithIdx[number] = idx    
            
            
            
        