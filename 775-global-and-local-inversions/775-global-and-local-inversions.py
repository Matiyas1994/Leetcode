class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        Max = float(-inf)
        n = len(nums)
        for i in range(n-2):
            Max = max(Max,nums[i])
            if Max > nums[i+2]:
                return False
        return True 
        
        
        
#         GlobalInv = 0
#         LocalInv = 0
        
#         def mergeSort(left,right):
#             if left >= right:
#                 return
#             mid = left + (right-left)//2
            
#             mergeSort(left, mid)
#             mergeSort(mid+1, right)
            
#             mergeboth(left, mid, right)
            
#         def mergeboth(left, mid, right):
#             nonlocal GlobalInv
#             arr1ptr, arr2ptr = left, mid+1
#             temp =[]
#             while arr1ptr <= mid and arr2ptr <= right:
#                 if nums[arr1ptr] <= nums[arr2ptr]:
#                     temp.append(nums[arr1ptr])
#                     arr1ptr +=1
#                 else:
#                     temp.append(nums[arr2ptr])
#                     arr2ptr +=1
#                     GlobalInv += (mid+1-arr1ptr)
            
#             while arr1ptr <= mid:
#                 temp.append(nums[arr1ptr])
#                 arr1ptr +=1
                
#             while  arr2ptr <= right:
#                 temp.append(nums[arr2ptr])
#                 arr2ptr +=1
            
#             for i in range(left,right+1):
#                 nums[i] = temp[i-left]
        
#         for i in range(len(nums)-1):
#             if nums[i] > nums[i+1]:
#                 LocalInv +=1
                
#         mergeSort(0,len(nums)-1)
#         return LocalInv == GlobalInv