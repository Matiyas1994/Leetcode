class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        
        while left <= right:
            mid = left + (right-left)//2
            
            if nums[mid]== target:
                return mid
            
            if nums[left] <= nums[mid]:
                if nums[left]<= target <= nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
            else:
                if nums[mid]<= target <= nums[right]:
                    left = mid+1
                else:
                    right = mid-1
                    
        return -1
                
        
#         def bs(L,R,targ):
#             while L <= R:
#                 mid = L + (R-L)//2
                
#                 if nums[mid] == targ:
#                     return mid
#                 elif nums[mid] > targ:
#                     R = mid - 1
#                 else:
#                     L = mid + 1
                    
#             return -1
# #        if  not rotated
#         if nums[0] < nums[-1]:
#             return bs(0,len(nums)-1,target)
# #     if rotated first we find the pivot point and determine were to look

#         L, R, piv =0, len(nums)-1, 0 
    
#         while L <= R:
#             mid = L + (R-L)//2
            
#             if mid == 0 or nums[mid] > nums[0]:
#                 L = mid + 1
#             else:
#                 piv = mid
#                 R = mid - 1
#         if nums[piv] <= target <=nums[-1]:
#             return bs(piv,len(nums)-1,target)
#         return bs(0,piv,target)
    
            
                