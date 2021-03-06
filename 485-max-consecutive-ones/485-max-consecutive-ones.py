class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
#         Max = 0
#         n = len(nums)
#         p2 = 0
        
#         while p2<n:
#             while p2<n and nums[p2] != 1: p2 +=1
            
#             p1 = p2
            
#             while p2<n and nums[p2]==1: p2 +=1
            
#             Max = max(Max,p2-p1)
        
#         return Max
        
        Max, count = 0, 0
        
        for num in nums:
            if num == 1:
                count +=1
                Max = max(Max,count)
            else:
                count = 0
        
        return Max