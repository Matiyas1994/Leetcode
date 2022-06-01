class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bs(L,R,targ):
            while L <= R:
                mid = L + (R-L)//2
                
                if nums[mid] == targ:
                    return mid
                elif nums[mid] > targ:
                    R = mid - 1
                else:
                    L = mid + 1
                    
            return -1
#        if  not rotated
        if nums[0] < nums[-1]:
            return bs(0,len(nums)-1,target)
#     if rotated first we find the pivot point and determine were to look

        L, R, piv =0, len(nums)-1, 0 
    
        while L <= R:
            mid = L + (R-L)//2
            
            if mid == 0 or nums[mid] > nums[0]:
                L = mid + 1
            else:
                piv = mid
                R = mid - 1
      
        return max(bs(0,piv,target),bs(piv,len(nums)-1,target))
    
            
                