class Solution:
    def missingNumber(self, nums: List[int]) -> int:
#         n = len(nums) + 1
#         s = 0
#         for num in nums:
#             s = s ^ num
#         return n - s
        nums.sort()
        numsLength = len(nums)
        if nums[-1] != numsLength:
            return numsLength
        for idx, val in enumerate(nums):
            if idx != val:
                return idx
        
        