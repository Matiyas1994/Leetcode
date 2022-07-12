class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        replacewith = [0,0]
        rStartIdx = 0
        n = len(nums)
        for i in range(n-1,0,-1):
            if nums[i] > nums[i-1]:
                rStartIdx = i
                replacewith[0],replacewith[1] = nums[i], i
                for j in range(i,n):
                    if nums[j] < replacewith[0] and nums[j] > nums[i-1]:
                        replacewith[0],replacewith[1] = nums[j], j
                nums[replacewith[1]] = nums[i-1]
                nums[i-1] = replacewith[0]
                break
        
        
        for k,val in enumerate(sorted(nums[rStartIdx:])):
            nums[k+rStartIdx] = val
                
        
#         t = sorted(nums)
#         if t[::-1] == nums:
#             nums.sort()
#             return
#         Min = [nums[-1],len(nums)-1]
#         for i in range(len(nums)-1,0,-1):
#             if nums[i] < Min[0]:
#                 Min[0],Min[1] = nums[i], i 
                
#             if nums[i] > nums[i-1]:
#                 nums[Min[1]] =  nums[i-1]
#                 nums[i-1] = Min[0]
#                 t2 = sorted(nums[i:])
#                 for k in range(len(t2)):
#                     nums[k+i] = t2[k]
#                 return
                    
                
                
                
            