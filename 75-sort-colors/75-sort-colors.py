class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        s, e, i = 0, len(nums)-1, 0
        
        while i <= e:
            if nums[i]==0:
                nums[i], nums[s] = nums[s], 0
                s +=1
                i +=1
            elif nums[i]==2:
                nums[i], nums[e] = nums[e], 2
                e -=1
            else:
                i +=1
                
                
        
        
        
        
        
        
        
        
        
#         colorsFreq = [0,0,0]
        
#         for n in nums:
#             colorsFreq[n] +=1
    
#         start = 0
#         for i in range(3):
#             for j in range(start, start+colorsFreq[i]):
#                 nums[j] = i
#             if colorsFreq[i] > 0: 
#                 start = j+1 
        