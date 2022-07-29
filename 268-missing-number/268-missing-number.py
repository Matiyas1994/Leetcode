class Solution:
    def missingNumber(self, nums: List[int]) -> int:

    #   """  BIt Manipulation with XOR """
    #  eg [3,0,4,1] = 4 ^ 0 ^ 3 ^ 1 ^ 0 ^ 2 ^ 4 ^ 3 ^ 1 = 2     
    
        res = 0
        for idx,num in enumerate(nums):
            res ^= num ^ (idx+1)
            
        return res 


    #   """ Using sort """
        # nums.sort()
        # numsLength = len(nums)
        # if nums[-1] != numsLength:
        #     return numsLength
        # for idx, val in enumerate(nums):
        #     if idx != val:
        #         return idx
        
        
        """Using Maths"""
        # n = len(nums)
        # sumOneUpToN = n * (n + 1)//2
        # sumOfTheArray = sum(nums)
        # return sumOneUpToN - sumOfTheArray